
import json
import os
import zlib
from io import BytesIO

from core.commands.remote.ac.base import AsyncCommandBase
from core.commands.remote.projectsync import PROJECT_SYNC_STAGE, ProjectSync


class ProjectSyncAsyncCmd(AsyncCommandBase):
    def __init__(self, *args, **kwargs):
        self.psync = None
        self._upstream = None
        super(ProjectSyncAsyncCmd, self).__init__(*args, **kwargs)

    def start(self):
        project_dir = os.path.join(
            self.options["agent_working_dir"], "projects", self.options["id"]
        )
        self.psync = ProjectSync(project_dir)
        for name in self.options["items"]:
            self.psync.add_item(os.path.join(project_dir, name), name)

    def stop(self):
        self.psync = None
        self._upstream = None
        self._return_code = PROJECT_SYNC_STAGE.COMPLETED.value

    def ac_write(self, data):
        stage = PROJECT_SYNC_STAGE.lookupByValue(data.get("stage"))

        if stage is PROJECT_SYNC_STAGE.DBINDEX:
            self.psync.rebuild_dbindex()
            return zlib.compress(json.dumps(self.psync.get_dbindex()).encode())

        if stage is PROJECT_SYNC_STAGE.DELETE:
            return self.psync.delete_dbindex(
                json.loads(zlib.decompress(data["dbindex"]))
            )

        if stage is PROJECT_SYNC_STAGE.UPLOAD:
            if not self._upstream:
                self._upstream = BytesIO()
            self._upstream.write(data["chunk"])
            if self._upstream.tell() == data["total"]:
                self.psync.decompress_items(self._upstream)
                self._upstream = None
                return PROJECT_SYNC_STAGE.EXTRACTED.value

            return PROJECT_SYNC_STAGE.UPLOAD.value

        return None
