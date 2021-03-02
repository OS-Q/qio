
from os.path import join

from platformio import proc
from platformio.commands.test.processor import TestProcessorBase
from platformio.proc import LineBufferedAsyncPipe


class NativeTestProcessor(TestProcessorBase):
    def process(self):
        if not self.options["without_building"]:
            self.print_progress("Building...")
            if not self.build_or_upload(["__test"]):
                return False
        if self.options["without_testing"]:
            return None
        self.print_progress("Testing...")
        return self.run()

    def run(self):
        build_dir = self.options["project_config"].get_optional_dir("build")
        result = proc.exec_command(
            [join(build_dir, self.env_name, "program")],
            stdout=LineBufferedAsyncPipe(self.on_run_out),
            stderr=LineBufferedAsyncPipe(self.on_run_out),
        )
        assert "returncode" in result
        return result["returncode"] == 0 and not self._run_failed
