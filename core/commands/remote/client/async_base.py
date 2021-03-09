
import click
from twisted.spread import pb  # pylint: disable=import-error

from core.commands.remote.client.base import RemoteClientBase


class AsyncClientBase(RemoteClientBase):
    def __init__(self, command, agents, options):
        RemoteClientBase.__init__(self)
        self.command = command
        self.agents = agents
        self.options = options

        self._acs_total = 0
        self._acs_ended = 0

    def agent_pool_ready(self):
        pass

    def cb_async_result(self, result):
        if self._acs_total == 0:
            self._acs_total = len(result)
        for (success, value) in result:
            if not success:
                raise pb.Error(value)
            self.acread_data(*value)

    def acread_data(self, agent_id, ac_id, agent_name=None):
        d = self.agentpool.callRemote("acread", agent_id, ac_id)
        d.addCallback(self.cb_acread_result, agent_id, ac_id, agent_name)
        d.addErrback(self.cb_global_error)

    def cb_acread_result(self, result, agent_id, ac_id, agent_name):
        if result is None:
            self.acclose(agent_id, ac_id)
        else:
            if self._acs_total > 1 and agent_name:
                click.echo("[%s] " % agent_name, nl=False)
            click.echo(result, nl=False)
            self.acread_data(agent_id, ac_id, agent_name)

    def acclose(self, agent_id, ac_id):
        d = self.agentpool.callRemote("acclose", agent_id, ac_id)
        d.addCallback(self.cb_acclose_result)
        d.addErrback(self.cb_global_error)

    def cb_acclose_result(self, exit_code):
        self._acs_ended += 1
        if self._acs_ended != self._acs_total:
            return
        self.disconnect(exit_code)
