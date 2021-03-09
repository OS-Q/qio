
import os

from core.compat import ci_strings_are_equal
from core.package.manager.platform import PlatformPackageManager
from core.package.meta import PackageSpec
from core.platform.factory import PlatformFactory
from core.project.config import ProjectConfig
from core.project.exception import InvalidProjectConfError


def get_builtin_libs(storage_names=None):
    # pylint: disable=import-outside-toplevel
    from core.package.manager.library import LibraryPackageManager

    items = []
    storage_names = storage_names or []
    pm = PlatformPackageManager()
    for pkg in pm.get_installed():
        p = PlatformFactory.new(pkg)
        for storage in p.get_lib_storages():
            if storage_names and storage["name"] not in storage_names:
                continue
            lm = LibraryPackageManager(storage["path"])
            items.append(
                {
                    "name": storage["name"],
                    "path": storage["path"],
                    "items": lm.legacy_get_installed(),
                }
            )
    return items


def is_builtin_lib(name, storages=None):
    for storage in storages or get_builtin_libs():
        for lib in storage["items"]:
            if lib.get("name") == name:
                return True
    return False


def ignore_deps_by_specs(deps, specs):
    result = []
    for dep in deps:
        depspec = PackageSpec(dep)
        if depspec.external:
            result.append(dep)
            continue
        ignore_conditions = []
        for spec in specs:
            if depspec.owner:
                ignore_conditions.append(
                    ci_strings_are_equal(depspec.owner, spec.owner)
                    and ci_strings_are_equal(depspec.name, spec.name)
                )
            else:
                ignore_conditions.append(ci_strings_are_equal(depspec.name, spec.name))
        if not any(ignore_conditions):
            result.append(dep)
    return result


def save_project_libdeps(project_dir, specs, environments=None, action="add"):
    config = ProjectConfig.get_instance(os.path.join(project_dir, "platform111.ini"))
    config.validate(environments)
    for env in config.envs():
        if environments and env not in environments:
            continue
        config.expand_interpolations = False
        candidates = []
        try:
            candidates = ignore_deps_by_specs(
                config.get("env:" + env, "lib_deps"), specs
            )
        except InvalidProjectConfError:
            pass
        if action == "add":
            candidates.extend(spec.as_dependency() for spec in specs)
        if candidates:
            result = []
            for item in candidates:
                item = item.strip()
                if item and item not in result:
                    result.append(item)
            config.set("env:" + env, "lib_deps", result)
        elif config.has_option("env:" + env, "lib_deps"):
            config.remove_option("env:" + env, "lib_deps")
    config.save()
