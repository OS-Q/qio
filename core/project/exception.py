
from core.exception import PlatformioException, UserSideException


class ProjectError(PlatformioException):
    pass


class NotPlatformIOProjectError(ProjectError, UserSideException):

    MESSAGE = (
        "Not a PlatformIO project. `platform111.ini` file has not been "
        "found in current working directory ({0}). To initialize new project "
        "please use `platformio project init` command"
    )


class InvalidProjectConfError(ProjectError, UserSideException):

    MESSAGE = "Invalid '{0}' (project configuration file): '{1}'"


class UndefinedEnvPlatformError(ProjectError, UserSideException):

    MESSAGE = "Please specify platform for '{0}' environment"


class ProjectEnvsNotAvailableError(ProjectError, UserSideException):

    MESSAGE = "Please setup environments in `platform111.ini` file"


class UnknownEnvNamesError(ProjectError, UserSideException):

    MESSAGE = "Unknown environment names '{0}'. Valid names are '{1}'"


class ProjectOptionValueError(ProjectError, UserSideException):

    MESSAGE = "{0} for option `{1}` in section [{2}]"
