
import click

from platformio.cache import cleanup_content_cache
from platformio.commands.lib.command import CTX_META_STORAGE_DIRS_KEY
from platformio.commands.lib.command import lib_update as cmd_lib_update
from platformio.commands.platform import platform_update as cmd_platform_update
from platformio.package.manager.core import update_core_packages
from platformio.package.manager.library import LibraryPackageManager


@click.command(
    "update", short_help="Update installed platforms, packages and libraries"
)
@click.option("--core-packages", is_flag=True, help="Update only the core packages")
@click.option(
    "-c",
    "--only-check",
    is_flag=True,
    help="DEPRECATED. Please use `--dry-run` instead",
)
@click.option(
    "--dry-run", is_flag=True, help="Do not update, only check for the new versions"
)
@click.pass_context
def cli(ctx, core_packages, only_check, dry_run):
    # cleanup lib search results, cached board and platform lists
    cleanup_content_cache("http")

    only_check = dry_run or only_check

    update_core_packages(only_check)

    if core_packages:
        return

    click.echo()
    click.echo("Platform Manager")
    click.echo("================")
    ctx.invoke(cmd_platform_update, only_check=only_check)

    click.echo()
    click.echo("Library Manager")
    click.echo("===============")
    ctx.meta[CTX_META_STORAGE_DIRS_KEY] = [LibraryPackageManager().package_dir]
    ctx.invoke(cmd_lib_update, only_check=only_check)
