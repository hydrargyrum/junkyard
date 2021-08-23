#!/usr/bin/env python3

"""
If you have multiple docker-compose.yml, there's a builtin merging (multiple
`-f`arguments ). If you use `build` in them, it will only consider the first
context directory it finds. https://github.com/docker/compose/issues/3874
All `context` or `dockerfile` keys will be relative to the first compose file
location, not to each compose file.
The solution is to use absolute paths. This script combines several compose
files into one and uses absolute paths. The original files are left untouched.

usage: merge-docker-compose-files.py foo/compose.yml bar/compose.yml
"""

from contextlib import ExitStack
from pathlib import Path
from subprocess import check_output
import sys
from tempfile import NamedTemporaryFile

import yaml


def replace_yaml(composein):
    """set absolute paths in yaml content, returns yaml string"""
    parent = composein.parent

    with composein.open() as fp:
        content = yaml.safe_load(fp)

    for service in content.get("services", {}).values():
        try:
            p = service["build"]["context"]
        except KeyError:
            pass
        else:
            service["build"]["context"] = str(parent / p)

        try:
            p = service["build"]["dockerfile"]
        except KeyError:
            pass
        else:
            service["build"]["dockerfile"] = str(parent / p)

        try:
            envs = service["env_file"]
        except KeyError:
            pass
        else:
            service["env_file"] = [str(parent / p) for p in envs]

    return yaml.dump(content)


cwd = Path.cwd().resolve()
stack = ExitStack()
outs = []

for composein in sys.argv[1:]:
    composein = Path(composein).resolve()

    content = replace_yaml(composein)

    # NamedTemporaryFile is normally used as a context manager.
    # But we can't stack an undefined number of context managers
    # so ExitStack comes to the rescue.
    temp = stack.enter_context(
        NamedTemporaryFile(
            dir=composein.parent, prefix=".compose.", suffix=".yml",
        )
    )
    outs.append(Path(temp.name))
    outs[-1].write_text(content)


# `docker-compose config` combines files (and expands vars etc.)
combined = check_output(
    ["docker-compose", *(f"--file={out}" for out in outs), "config"],
    encoding="utf-8"
)
# finally write output file
Path("combined-docker-compose.yml").write_text(combined)
