
import serial

from platformio.commands.device import DeviceMonitorFilter


class Hexlify(DeviceMonitorFilter):
    NAME = "hexlify"

    def __init__(self, *args, **kwargs):
        super(Hexlify, self).__init__(*args, **kwargs)
        self._counter = 0

    def rx(self, text):
        result = ""
        for b in serial.iterbytes(text):
            if (self._counter % 16) == 0:
                result += "\n{:04X} | ".format(self._counter)
            asciicode = ord(b)
            if asciicode <= 255:
                result += "{:02X} ".format(asciicode)
            else:
                result += "?? "
            self._counter += 1
        return result
