# Copyright (c) 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import socket

from starlette.concurrency import run_in_threadpool

from qio import util
from qio.compat import IS_WINDOWS
from qio.http import HTTPSession
from qio.proc import where_is_program


class AsyncSession(HTTPSession):
    async def request(  # pylint: disable=signature-differs,invalid-overridden-method
        self, *args, **kwargs
    ):
        func = super().request
        return await run_in_threadpool(func, *args, **kwargs)


@util.memoized(expire="60s")
def requests_session():
    return AsyncSession()


@util.memoized(expire="60s")
def get_core_fullpath():
    return where_is_program("platformio" + (".exe" if IS_WINDOWS else ""))


def is_port_used(host, port):
    socket.setdefaulttimeout(1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if IS_WINDOWS:
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
