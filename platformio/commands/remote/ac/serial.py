
from time import sleep

from twisted.internet import protocol, reactor  # pylint: disable=import-error
from twisted.internet.serialport import SerialPort  # pylint: disable=import-error

from platformio.commands.remote.ac.base import AsyncCommandBase


class SerialPortAsyncCmd(protocol.Protocol, AsyncCommandBase):
    def start(self):
        SerialPort(
            self,
            reactor=reactor,
            **{
                "deviceNameOrPortNumber": self.options["port"],
                "baudrate": self.options["baud"],
                "parity": self.options["parity"],
                "rtscts": 1 if self.options["rtscts"] else 0,
                "xonxoff": 1 if self.options["xonxoff"] else 0,
            }
        )

    def connectionMade(self):
        self.reset_device()
        if self.options.get("rts", None) is not None:
            self.transport.setRTS(self.options.get("rts"))
        if self.options.get("dtr", None) is not None:
            self.transport.setDTR(self.options.get("dtr"))

    def reset_device(self):
        self.transport.flushInput()
        self.transport.setDTR(False)
        self.transport.setRTS(False)
        sleep(0.1)
        self.transport.setDTR(True)
        self.transport.setRTS(True)
        sleep(0.1)

    def dataReceived(self, data):
        self._ac_ondata(data)

    def connectionLost(self, reason):  # pylint: disable=unused-argument
        if self._paused:
            return
        self._return_code = 0
        self._ac_ended()
