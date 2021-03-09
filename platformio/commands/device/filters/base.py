
from serial.tools import miniterm

from platformio.project.config import ProjectConfig


class DeviceMonitorFilter(miniterm.Transform):
    def __init__(self, options=None):
        """ Called by PlatformIO to pass context """
        miniterm.Transform.__init__(self)

        self.options = options or {}
        self.project_dir = self.options.get("project_dir")
        self.environment = self.options.get("environment")

        self.config = ProjectConfig.get_instance()
        if not self.environment:
            default_envs = self.config.default_envs()
            if default_envs:
                self.environment = default_envs[0]
            elif self.config.envs():
                self.environment = self.config.envs()[0]

    def __call__(self):
        """ Called by the miniterm library when the filter is actually used """
        return self

    @property
    def NAME(self):
        raise NotImplementedError("Please declare NAME attribute for the filter class")
