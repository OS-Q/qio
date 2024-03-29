# Copyright (c) 2014-present PlatformIO <contact@platformio.org>
# Copyright 2020 MongoDB Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# pylint: disable=unused-argument, protected-access, unused-variable, import-error
# Original: https://github.com/mongodb/mongo/blob/master/site_scons/site_tools/compilation_db.py

import itertools
import json
import os

import SCons

from qio.builder.tools.piobuild import SRC_ASM_EXT, SRC_C_EXT, SRC_CXX_EXT
from qio.proc import where_is_program

# Implements the ability for SCons to emit a compilation database for the MongoDB project. See
# http://clang.llvm.org/docs/JSONCompilationDatabase.html for details on what a compilation
# database is, and why you might want one. The only user visible entry point here is
# 'env.CompilationDatabase'. This method takes an optional 'target' to name the file that
# should hold the compilation database, otherwise, the file defaults to compile_commands.json,
# which is the name that most clang tools search for by default.

# Is there a better way to do this than this global? Right now this exists so that the
# emitter we add can record all of the things it emits, so that the scanner for the top level
# compilation database can access the complete list, and also so that the writer has easy
# access to write all of the files. But it seems clunky. How can the emitter and the scanner
# communicate more gracefully?
__COMPILATION_DB_ENTRIES = []


# We make no effort to avoid rebuilding the entries. Someday, perhaps we could and even
# integrate with the cache, but there doesn't seem to be much call for it.
class __CompilationDbNode(SCons.Node.Python.Value):
    def __init__(self, value):
        SCons.Node.Python.Value.__init__(self, value)
        self.Decider(changed_since_last_build_node)


def changed_since_last_build_node(*args, **kwargs):
    """Dummy decider to force always building"""
    return True


def makeEmitCompilationDbEntry(comstr):
    """
    Effectively this creates a lambda function to capture:
    * command line
    * source
    * target
    :param comstr: unevaluated command line
    :return: an emitter which has captured the above
    """
    user_action = SCons.Action.Action(comstr)

    def EmitCompilationDbEntry(target, source, env):
        """
        This emitter will be added to each c/c++ object build to capture the info needed
        for clang tools
        :param target: target node(s)
        :param source: source node(s)
        :param env: Environment for use building this node
        :return: target(s), source(s)
        """

        # Resolve absolute path of toolchain
        for cmd in ("CC", "CXX", "AS"):
            if cmd not in env:
                continue
            if os.path.isabs(env[cmd]):
                continue
            env[cmd] = where_is_program(
                env.subst("$%s" % cmd), env.subst("${ENV['PATH']}")
            )

        dbtarget = __CompilationDbNode(source)

        entry = env.__COMPILATIONDB_Entry(
            target=dbtarget,
            source=[],
            __COMPILATIONDB_UTARGET=target,
            __COMPILATIONDB_USOURCE=source,
            __COMPILATIONDB_UACTION=user_action,
            __COMPILATIONDB_ENV=env,
        )

        # Technically, these next two lines should not be required: it should be fine to
        # cache the entries. However, they don't seem to update properly. Since they are quick
        # to re-generate disable caching and sidestep this problem.
        env.AlwaysBuild(entry)
        env.NoCache(entry)

        __COMPILATION_DB_ENTRIES.append(dbtarget)

        return target, source

    return EmitCompilationDbEntry


def CompilationDbEntryAction(target, source, env, **kw):
    """
    Create a dictionary with evaluated command line, target, source
    and store that info as an attribute on the target
    (Which has been stored in __COMPILATION_DB_ENTRIES array
    :param target: target node(s)
    :param source: source node(s)
    :param env: Environment for use building this node
    :param kw:
    :return: None
    """

    command = env["__COMPILATIONDB_UACTION"].strfunction(
        target=env["__COMPILATIONDB_UTARGET"],
        source=env["__COMPILATIONDB_USOURCE"],
        env=env["__COMPILATIONDB_ENV"],
    )

    entry = {
        "directory": env.Dir("#").abspath,
        "command": command,
        "file": str(env["__COMPILATIONDB_USOURCE"][0]),
    }

    target[0].write(entry)


def WriteCompilationDb(target, source, env):
    entries = []

    for s in __COMPILATION_DB_ENTRIES:
        item = s.read()
        item["file"] = os.path.abspath(item["file"])
        entries.append(item)

    with open(str(target[0]), mode="w", encoding="utf8") as target_file:
        json.dump(
            entries, target_file, sort_keys=True, indent=4, separators=(",", ": ")
        )


def ScanCompilationDb(node, env, path):
    return __COMPILATION_DB_ENTRIES


def generate(env, **kwargs):
    static_obj, shared_obj = SCons.Tool.createObjBuilders(env)

    env["COMPILATIONDB_COMSTR"] = kwargs.get(
        "COMPILATIONDB_COMSTR", "Building compilation database $TARGET"
    )

    components_by_suffix = itertools.chain(
        itertools.product(
            [".%s" % ext for ext in SRC_C_EXT],
            [
                (static_obj, SCons.Defaults.StaticObjectEmitter, "$CCCOM"),
                (shared_obj, SCons.Defaults.SharedObjectEmitter, "$SHCCCOM"),
            ],
        ),
        itertools.product(
            [".%s" % ext for ext in SRC_CXX_EXT],
            [
                (static_obj, SCons.Defaults.StaticObjectEmitter, "$CXXCOM"),
                (shared_obj, SCons.Defaults.SharedObjectEmitter, "$SHCXXCOM"),
            ],
        ),
        itertools.product(
            [".%s" % ext for ext in SRC_ASM_EXT],
            [(static_obj, SCons.Defaults.StaticObjectEmitter, "$ASCOM")],
        ),
    )

    for entry in components_by_suffix:
        suffix = entry[0]
        builder, base_emitter, command = entry[1]

        # Assumes a dictionary emitter
        emitter = builder.emitter[suffix]
        builder.emitter[suffix] = SCons.Builder.ListEmitter(
            [emitter, makeEmitCompilationDbEntry(command)]
        )

    env["BUILDERS"]["__COMPILATIONDB_Entry"] = SCons.Builder.Builder(
        action=SCons.Action.Action(CompilationDbEntryAction, None),
    )

    env["BUILDERS"]["__COMPILATIONDB_Database"] = SCons.Builder.Builder(
        action=SCons.Action.Action(WriteCompilationDb, "$COMPILATIONDB_COMSTR"),
        target_scanner=SCons.Scanner.Scanner(
            function=ScanCompilationDb, node_class=None
        ),
    )

    def CompilationDatabase(env, target):
        result = env.__COMPILATIONDB_Database(target=target, source=[])

        env.AlwaysBuild(result)
        env.NoCache(result)

        return result

    env.AddMethod(CompilationDatabase, "CompilationDatabase")


def exists(env):
    return True
