
from core.commands.device import DeviceMonitorFilter


class SendOnEnter(DeviceMonitorFilter):
    NAME = "send_on_enter"

    def __init__(self, *args, **kwargs):
        super(SendOnEnter, self).__init__(*args, **kwargs)
        self._buffer = ""

        if self.options.get("eol") == "CR":
            self._eol = "\r"
        elif self.options.get("eol") == "LF":
            self._eol = "\n"
        else:
            self._eol = "\r\n"

    def tx(self, text):
        self._buffer += text
        if self._buffer.endswith(self._eol):
            text = self._buffer[: len(self._eol) * -1]
            self._buffer = ""
            return text
        return ""
