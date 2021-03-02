from platformio.exception import PlatformioException, UserSideException


class DebugError(PlatformioException):
    pass


class DebugSupportError(DebugError, UserSideException):

    MESSAGE = (
        "Currently, PlatformIO does not support debugging for `{0}`.\n"
        "Please request support at https://github.com/platformio/"
        "platformio-core/issues \nor visit -> https://docs.platformio.org"
        "/page/plus/debugging.html"
    )


class DebugInvalidOptionsError(DebugError, UserSideException):
    pass
