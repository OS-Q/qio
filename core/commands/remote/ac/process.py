
import os

from twisted.internet import protocol, reactor  # pylint: disable=import-error

from core.commands.remote.ac.base import AsyncCommandBase


class ProcessAsyncCmd(protocol.ProcessProtocol, AsyncCommandBase):
    def start(self):
        env = dict(os.environ).copy()
        env.update({"PLATFORMIO_FORCE_ANSI": "true"})
        reactor.spawnProcess(
            self, self.options["executable"], self.options["args"], env
        )

    def outReceived(self, data):
        self._ac_ondata(data)

    def errReceived(self, data):
        self._ac_ondata(data)

    def processExited(self, reason):
        self._return_code = reason.value.exitCode

    def processEnded(self, reason):
        if self._return_code is None:
            self._return_code = reason.value.exitCode
        self._ac_ended()
