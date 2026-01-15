#!/usr/bin/env python3

import argparse
import re
import subprocess
import sys


def run(cmd: str) -> str:
    return subprocess.check_output(cmd, shell=True, text=True).strip()


def get_prev_version(version: str) -> str:
    major, minor = version.split(".")[:2]
    tags = run(
        "git tag --sort=version:refname | grep -E '^[0-9]+\\.[0-9]+\\.[0-9]+$' "
    ).splitlines()

    prev = None
    for tag in tags:
        t_major, t_minor, _ = tag.split(".")
        if (t_major, t_minor) < (major, minor):
            prev = tag

    return prev or "0.1.0"


def get_range_end(version: str) -> str:
    try:
        run(f"git rev-parse {version}")
    except subprocess.CalledProcessError:
        print(f"Error: tag {version} does not exist", file=sys.stderr)
        sys.exit(1)
    return version


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    args = parser.parse_args()

    version = args.version
    if not re.match(r"^[0-9]+\.[0-9]+\.[0-9]+$", version):
        print(
            f"Error: Version {version} is not a full semantic version (X.Y.Z)",
            file=sys.stderr,
        )
        sys.exit(1)
    prev = get_prev_version(version)
    end = get_range_end(version)

    major_minor = ".".join(version.split(".")[:2])

    print(f"Previous version : {prev}")
    print(f"Range end        : {end}")
    print(f"Generating changelog for {prev}..{end}")

    subprocess.check_call(
        [
            "uv",
            "run",
            "git-cliff",
            f"{prev}..{end}",
            "-o",
            f"CHANGELOG/CHANGELOG-{major_minor}.md",
        ]
    )

    print(f"Changelog generated at CHANGELOG/CHANGELOG-{major_minor}.md")


if __name__ == "__main__":
    main()
