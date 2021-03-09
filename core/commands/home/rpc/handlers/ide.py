
import time

import jsonrpc

from core.compat import get_running_loop


class IDERPC:
    def __init__(self):
        self._queue = {}

    def send_command(self, sid, command, params):
        if not self._queue.get(sid):
            raise jsonrpc.exceptions.JSONRPCDispatchException(
                code=4005, message="PIO Home IDE agent is not started"
            )
        while self._queue[sid]:
            self._queue[sid].pop().set_result(
                {"id": time.time(), "method": command, "params": params}
            )

    def listen_commands(self, sid=0):
        if sid not in self._queue:
            self._queue[sid] = []
        self._queue[sid].append(get_running_loop().create_future())
        return self._queue[sid][-1]

    def open_project(self, sid, project_dir):
        return self.send_command(sid, "open_project", project_dir)

    def open_text_document(self, sid, path, line=None, column=None):
        return self.send_command(
            sid, "open_text_document", dict(path=path, line=line, column=column)
        )
