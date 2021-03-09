
import re

import semantic_version


def cast_version_to_semver(value, force=True, raise_exception=False):
    assert value
    try:
        return semantic_version.Version(value)
    except ValueError:
        pass
    if force:
        try:
            return semantic_version.Version.coerce(value)
        except ValueError:
            pass
    if raise_exception:
        raise ValueError("Invalid SemVer version %s" % value)
    # parse commit hash
    if re.match(r"^[\da-f]+$", value, flags=re.I):
        return semantic_version.Version("0.0.0+sha." + value)
    return semantic_version.Version("0.0.0+" + value)


def pepver_to_semver(pepver):
    return cast_version_to_semver(
        re.sub(r"(\.\d+)\.?(dev|a|b|rc|post)", r"\1-\2.", pepver, 1)
    )


def get_original_version(version):
    if version.count(".") != 2:
        return None
    _, raw = version.split(".")[:2]
    if int(raw) <= 99:
        return None
    if int(raw) <= 9999:
        return "%s.%s" % (raw[:-2], int(raw[-2:]))
    return "%s.%s.%s" % (raw[:-4], int(raw[-4:-2]), int(raw[-2:]))
