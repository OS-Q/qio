
from __future__ import absolute_import

import hashlib
import os
import re

from SCons.Platform import TempFileMunge  # pylint: disable=import-error
from SCons.Subst import quote_spaces  # pylint: disable=import-error

from platformio.compat import WINDOWS, hashlib_encode_data

# There are the next limits depending on a platform:
# - Windows = 8192
# - Unix    = 131072
# We need ~512 characters for compiler and temporary file paths
MAX_LINE_LENGTH = (8192 if WINDOWS else 131072) - 512

WINPATHSEP_RE = re.compile(r"\\([^\"'\\]|$)")


def tempfile_arg_esc_func(arg):
    arg = quote_spaces(arg)
    if not WINDOWS:
        return arg
    # GCC requires double Windows slashes, let's use UNIX separator
    return WINPATHSEP_RE.sub(r"/\1", arg)


def long_sources_hook(env, sources):
    _sources = str(sources).replace("\\", "/")
    if len(str(_sources)) < MAX_LINE_LENGTH:
        return sources

    # fix space in paths
    data = []
    for line in _sources.split(".o "):
        line = line.strip()
        if not line.endswith(".o"):
            line += ".o"
        data.append('"%s"' % line)

    return '@"%s"' % _file_long_data(env, " ".join(data))


def _file_long_data(env, data):
    build_dir = env.subst("$BUILD_DIR")
    if not os.path.isdir(build_dir):
        os.makedirs(build_dir)
    tmp_file = os.path.join(
        build_dir, "longcmd-%s" % hashlib.md5(hashlib_encode_data(data)).hexdigest()
    )
    if os.path.isfile(tmp_file):
        return tmp_file
    with open(tmp_file, "w") as fp:
        fp.write(data)
    return tmp_file


def exists(_):
    return True


def generate(env):
    kwargs = dict(
        _long_sources_hook=long_sources_hook,
        TEMPFILE=TempFileMunge,
        MAXLINELENGTH=MAX_LINE_LENGTH,
        TEMPFILEARGESCFUNC=tempfile_arg_esc_func,
        TEMPFILESUFFIX=".tmp",
        TEMPFILEDIR="$BUILD_DIR",
    )

    for name in ("LINKCOM", "ASCOM", "ASPPCOM", "CCCOM", "CXXCOM"):
        kwargs[name] = "${TEMPFILE('%s','$%sSTR')}" % (env.get(name), name)

    kwargs["ARCOM"] = env.get("ARCOM", "").replace(
        "$SOURCES", "${_long_sources_hook(__env__, SOURCES)}"
    )
    env.Replace(**kwargs)

    return env
