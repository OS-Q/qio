
from platformio import exception
from platformio.commands.check.tools.clangtidy import ClangtidyCheckTool
from platformio.commands.check.tools.cppcheck import CppcheckCheckTool
from platformio.commands.check.tools.pvsstudio import PvsStudioCheckTool


class CheckToolFactory(object):
    @staticmethod
    def new(tool, project_dir, config, envname, options):
        cls = None
        if tool == "cppcheck":
            cls = CppcheckCheckTool
        elif tool == "clangtidy":
            cls = ClangtidyCheckTool
        elif tool == "pvs-studio":
            cls = PvsStudioCheckTool
        else:
            raise exception.PlatformioException("Unknown check tool `%s`" % tool)
        return cls(project_dir, config, envname, options)
