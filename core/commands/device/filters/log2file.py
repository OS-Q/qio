
import io
import os.path
from datetime import datetime

from platformio.commands.device import DeviceMonitorFilter


class LogToFile(DeviceMonitorFilter):
    NAME = "log2file"

    def __init__(self, *args, **kwargs):
        super(LogToFile, self).__init__(*args, **kwargs)
        self._log_fp = None

    def __call__(self):
        log_file_name = "platformio-device-monitor-%s.log" % datetime.now().strftime(
            "%y%m%d-%H%M%S"
        )
        print("--- Logging an output to %s" % os.path.abspath(log_file_name))
        self._log_fp = io.open(log_file_name, "w", encoding="utf-8")
        return self

    def __del__(self):
        if self._log_fp:
            self._log_fp.close()

    def rx(self, text):
        self._log_fp.write(text)
        self._log_fp.flush()
        return text
