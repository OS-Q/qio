
from platformio.package.manager.base import BasePackageManager
from platformio.package.meta import PackageType
from platformio.project.config import ProjectConfig


class ToolPackageManager(BasePackageManager):  # pylint: disable=too-many-ancestors
    def __init__(self, package_dir=None):
        if not package_dir:
            package_dir = ProjectConfig.get_instance().get_optional_dir("packages")
        super(ToolPackageManager, self).__init__(PackageType.TOOL, package_dir)

    @property
    def manifest_names(self):
        return PackageType.get_manifest_map()[PackageType.TOOL]
