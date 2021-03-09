
from platformio.commands.remote.client.async_base import AsyncClientBase


class UpdateCoreClient(AsyncClientBase):
    def agent_pool_ready(self):
        d = self.agentpool.callRemote("cmd", self.agents, self.command, self.options)
        d.addCallback(self.cb_async_result)
        d.addErrback(self.cb_global_error)
