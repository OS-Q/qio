
import socket

import requests
from starlette.concurrency import run_in_threadpool

from platformio import util
from platformio.compat import WINDOWS
from platformio.proc import where_is_program


class AsyncSession(requests.Session):
    async def request(  # pylint: disable=signature-differs,invalid-overridden-method
        self, *args, **kwargs
    ):
        func = super(AsyncSession, self).request
        return await run_in_threadpool(func, *args, **kwargs)


@util.memoized(expire="60s")
def requests_session():
    return AsyncSession()


@util.memoized(expire="60s")
def get_core_fullpath():
    return where_is_program(
        "platformio" + (".exe" if "windows" in util.get_systype() else "")
    )


def is_port_used(host, port):
    socket.setdefaulttimeout(1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if WINDOWS:
        try:
            s.bind((host, port))
            s.close()
            return False
        except (OSError, socket.error):
            pass
    else:
        try:
            s.connect((host, port))
            s.close()
        except socket.error:
            return False

    return True
