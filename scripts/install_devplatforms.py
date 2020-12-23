
import json
import subprocess
import sys

import click


@click.command()
@click.option("--desktop", is_flag=True, default=False)
@click.option(
    "--names",
    envvar="PIO_INSTALL_DEVPLATFORM_NAMES",
    help="Install specified platform (split by comma)",
)
@click.option(
    "--ownernames",
    envvar="PIO_INSTALL_DEVPLATFORM_OWNERNAMES",
    help="Filter by ownernames (split by comma)",
)
def main(desktop, names, ownernames):
    platforms = json.loads(
        subprocess.check_output(["pio", "platform", "search", "--json-output"]).decode()
    )
    names = [n.strip() for n in (names or "").split(",") if n.strip()]
    ownernames = [n.strip() for n in (ownernames or "").split(",") if n.strip()]
    for platform in platforms:
        skip = [
            not desktop and platform["forDesktop"],
            names and platform["name"] not in names,
            ownernames and platform["ownername"] not in ownernames,
        ]
        if any(skip):
            continue
        subprocess.check_call(
            [
                "pio",
                "pkg",
                "install",
                "--global",
                "--skip-dependencies",
                "--platform",
                "{ownername}/{name}".format(**platform),
            ]
        )


if __name__ == "__main__":
    sys.exit(main())
