
from datetime import datetime

import click

from platformio.commands.remote.client.base import RemoteClientBase


class AgentListClient(RemoteClientBase):
    def agent_pool_ready(self):
        d = self.agentpool.callRemote("list", True)
        d.addCallback(self._cbResult)
        d.addErrback(self.cb_global_error)

    def _cbResult(self, result):
        for item in result:
            click.secho(item["name"], fg="cyan")
            click.echo("-" * len(item["name"]))
            click.echo("ID: %s" % item["id"])
            click.echo(
                "Started: %s"
                % datetime.fromtimestamp(item["started"]).strftime("%Y-%m-%d %H:%M:%S")
            )
            click.echo("")
        self.disconnect()
