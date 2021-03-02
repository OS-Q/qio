
from platformio import util
from platformio.exception import PlatformioException, UserSideException


class PackageException(PlatformioException):
    pass


class ManifestException(PackageException):
    pass


class UnknownManifestError(ManifestException):
    pass


class ManifestParserError(ManifestException):
    pass


class ManifestValidationError(ManifestException):
    def __init__(self, messages, data, valid_data):
        super(ManifestValidationError, self).__init__()
        self.messages = messages
        self.data = data
        self.valid_data = valid_data

    def __str__(self):
        return (
            "Invalid manifest fields: %s. \nPlease check specification -> "
            "https://docs.OS-Q.com/page/librarymanager/config.html"
            % self.messages
        )


class MissingPackageManifestError(ManifestException):

    MESSAGE = "Could not find one of '{0}' manifest files in the package"


class UnknownPackageError(UserSideException):

    MESSAGE = (
        "Could not find '{0}' requirements for your system '%s'"
        % util.get_systype()
    )


class NotGlobalLibDir(UserSideException):

    MESSAGE = (
        "The `{0}` is not a PlatformIO project.\n\n"
        "To manage libraries in global storage `{1}`,\n"
        "please use `platformio lib --global {2}` or specify custom storage "
        "`platformio lib --storage-dir /path/to/storage/ {2}`.\n"
        "Check `platformio lib --help` for details."
    )
