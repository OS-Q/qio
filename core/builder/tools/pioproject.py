
from __future__ import absolute_import

from core.project.config import MISSING, ProjectConfig, ProjectOptions


def GetProjectConfig(env):
    return ProjectConfig.get_instance(env["PROJECT_CONFIG"])


def GetProjectOptions(env, as_dict=False):
    return env.GetProjectConfig().items(env=env["PIOENV"], as_dict=as_dict)


def GetProjectOption(env, option, default=MISSING):
    return env.GetProjectConfig().get("env:" + env["PIOENV"], option, default)


def LoadProjectOptions(env):
    for option, value in env.GetProjectOptions():
        option_meta = ProjectOptions.get("env." + option)
        if (
            not option_meta
            or not option_meta.buildenvvar
            or option_meta.buildenvvar in env
        ):
            continue
        env[option_meta.buildenvvar] = value


def exists(_):
    return True


def generate(env):
    env.AddMethod(GetProjectConfig)
    env.AddMethod(GetProjectOptions)
    env.AddMethod(GetProjectOption)
    env.AddMethod(LoadProjectOptions)
    return env
