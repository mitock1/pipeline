#!/usr/bin/env python
# strip continuations and comments from a requirements file for formatting
import sys
from pathlib import Path
from traceback import print_exc
from typing import List

import yaml


def combine_continuations(lines):
    q: List[str] = []
    for line in lines:
        if line[0] == "\n":
            # blank line
            continue
        if line[-2] == "\\":
            # continued line
            q.append(line[:-2])
            continue
        elif len(q):
            # end of continued lines
            new_line = " ".join(q) + " " + line
            q[:] = []
        else:
            # normal line
            new_line = line
        yield new_line


def strip_comments(lines):
    for line in lines:
        if line[0] == "#":
            # starting comment
            continue
        index = line.find(" #")
        if index >= 0:
            # comment at end of line
            yield line[:index]
        else:
            # no comments
            yield line


def strip_spaces(lines):
    for line in lines:
        yield line.strip()


def parse_additional_options(lines):
    """split lines like --trusted-repo foo.com into separate lines"""
    q: List[str] = []
    for line in lines:
        splits = line.split()
        for split in splits:
            if split[0] == "-":
                if q:
                    yield " ".join(q)
                    q[:] = []
                yield split
            else:
                q.append(split)
        if q:
            yield " ".join(q)
            q[:] = []


def parse_reqs(lines):
    # pip combines continuations before stripping comments
    yield from parse_additional_options(
        strip_spaces(strip_comments(combine_continuations(lines)))
    )


def main():
    try:
        requirements_path = Path("requirements.txt")
        config_path = Path(".pre-commit-config.yaml")

        with requirements_path.open() as requirements_file:
            requirements = list(parse_reqs(requirements_file.readlines()))[2:]
        with config_path.open() as config_file:
            config = yaml.safe_load(config_file)

        mypy_repo = [repo for repo in config["repos"] if "mypy" in repo["repo"]][0]
        mypy_repo["hooks"][0]["additional_dependencies"] = requirements
        with config_path.open("w") as config_file:
            yaml.dump(config, config_file)
        return 0
    except Exception:
        print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
