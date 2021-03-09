
import signal
import time

import click
from twisted.internet import protocol  # pylint: disable=import-error

from core import fs
from core.compat import string_types
from core.proc import get_pythonexe_path
from core.project.helpers import get_project_core_dir


class BaseProcess(protocol.ProcessProtocol, object):

    STDOUT_CHUNK_SIZE = 2048
    LOG_FILE = None

    COMMON_PATTERNS = {
        "PLATFORMIO_HOME_DIR": get_project_core_dir(),
        "PLATFORMIO_CORE_DIR": get_project_core_dir(),
        "PYTHONEXE": get_pythonexe_path(),
    }

    def __init__(self):
        self._last_activity = 0

    def apply_patterns(self, source, patterns=None):
        _patterns = self.COMMON_PATTERNS.copy()
        _patterns.update(patterns or {})

        for key, value in _patterns.items():
            if key.endswith(("_DIR", "_PATH")):
                _patterns[key] = fs.to_unix_path(value)

        def _replace(text):
            for key, value in _patterns.items():
                pattern = "$%s" % key
                text = text.replace(pattern, value or "")
            return text

        if isinstance(source, string_types):
            source = _replace(source)
        elif isinstance(source, (list, dict)):
            items = enumerate(source) if isinstance(source, list) else source.items()
            for key, value in items:
                if isinstance(value, string_types):
                    source[key] = _replace(value)
                elif isinstance(value, (list, dict)):
                    source[key] = self.apply_patterns(value, patterns)

        return source

    def onStdInData(self, data):
        self._last_activity = time.time()
        if self.LOG_FILE:
            with open(self.LOG_FILE, "ab") as fp:
                fp.write(data)

    def outReceived(self, data):
        self._last_activity = time.time()
        if self.LOG_FILE:
            with open(self.LOG_FILE, "ab") as fp:
                fp.write(data)
        while data:
            chunk = data[: self.STDOUT_CHUNK_SIZE]
            click.echo(chunk, nl=False)
            data = data[self.STDOUT_CHUNK_SIZE :]

    def errReceived(self, data):
        self._last_activity = time.time()
        if self.LOG_FILE:
            with open(self.LOG_FILE, "ab") as fp:
                fp.write(data)
        click.echo(data, nl=False, err=True)

    def processEnded(self, _):
        self._last_activity = time.time()
        # Allow terminating via SIGINT/CTRL+C
        signal.signal(signal.SIGINT, signal.default_int_handler)
