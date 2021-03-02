
import os
import shutil

import click

from platformio import fs
from platformio.package.exception import UnknownPackageError
from platformio.package.meta import PackageSpec


class PackageManagerUninstallMixin(object):
    def uninstall(self, spec, silent=False, skip_dependencies=False):
        try:
            self.lock()
            return self._uninstall(spec, silent, skip_dependencies)
        finally:
            self.unlock()

    def _uninstall(self, spec, silent=False, skip_dependencies=False):
        pkg = self.get_package(spec)
        if not pkg or not pkg.metadata:
            raise UnknownPackageError(spec)

        if not silent:
            self.print_message(
                "Removing %s @ %s"
                % (click.style(pkg.metadata.name, fg="cyan"), pkg.metadata.version),
            )

        # firstly, remove dependencies
        if not skip_dependencies:
            self.uninstall_dependencies(pkg, silent)

        if os.path.islink(pkg.path):
            os.unlink(pkg.path)
        else:
            fs.rmtree(pkg.path)
        self.memcache_reset()

        # unfix detached-package with the same name
        detached_pkg = self.get_package(PackageSpec(name=pkg.metadata.name))
        if (
            detached_pkg
            and "@" in detached_pkg.path
            and not os.path.isdir(
                os.path.join(self.package_dir, detached_pkg.get_safe_dirname())
            )
        ):
            shutil.move(
                detached_pkg.path,
                os.path.join(self.package_dir, detached_pkg.get_safe_dirname()),
            )
            self.memcache_reset()

        if not silent:
            self.print_message(
                "{name} @ {version} has been removed!".format(**pkg.metadata.as_dict()),
                fg="green",
            )

        return pkg

    def uninstall_dependencies(self, pkg, silent=False):
        pass
