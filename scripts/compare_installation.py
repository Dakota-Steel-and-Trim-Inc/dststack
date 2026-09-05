#!/usr/bin/env python3
"""Compare installed DST skills and recorded sources without changing files."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys


EXPECTED_SOURCE = "dakota-steel-and-trim-inc/dststack"
IGNORED = {".git", "__pycache__", ".DS_Store"}


def source_name(value: str) -> str:
    match = re.fullmatch(
        r"(?:git@github\.com:|https://github\.com/|ssh://git@github\.com/)?"
        r"([\w.-]+/[\w.-]+?)(?:\.git)?/?", value, re.IGNORECASE,
    )
    return match.group(1).lower() if match else "unrecognized"


def snapshot(directory: Path) -> dict[str, str]:
    root = directory.resolve(strict=True)
    if not root.is_dir():
        raise ValueError(f"Expected a skill directory: {directory}")
    files = {}

    def walk_error(error: OSError) -> None:
        raise error

    for parent, dirs, names in os.walk(root, onerror=walk_error):
        dirs[:] = sorted(d for d in dirs if d not in IGNORED)
        for name in dirs + sorted(names):
            if name in IGNORED or name.endswith((".pyc", ".pyo")):
                continue
            path = Path(parent) / name
            relative = path.relative_to(root).as_posix()
            if path.is_symlink():
                raise ValueError(f"Cannot compare nested symlink: {directory / relative}")
            if name in dirs:
                continue
            if not path.is_file():
                raise ValueError(f"Cannot compare non-file: {directory / relative}")
            files[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    return files


def read_sources(lock_file: Path) -> dict[str, dict]:
    if not lock_file.exists():
        return {}
    try:
        data = json.loads(lock_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        raise ValueError("Invalid installation lock JSON") from None
    if not isinstance(data, dict) or not isinstance(data.get("skills"), dict):
        raise ValueError("Installation lock must contain a skills object")
    for entry in data["skills"].values():
        if not isinstance(entry, dict) or not isinstance(entry.get("source", ""), str):
            raise ValueError("Invalid skill source entry in installation lock")
    return data["skills"]


def compare(source_dir: Path, installed_dir: Path, lock_file: Path) -> dict:
    if not source_dir.is_dir():
        raise ValueError("Source skills directory is missing")
    skills = sorted(p for p in source_dir.iterdir() if p.is_dir())
    if not skills or any(not (p / "SKILL.md").is_file() for p in skills):
        raise ValueError("Source must contain skill directories with SKILL.md entrypoints")
    if installed_dir.exists() and not installed_dir.is_dir():
        raise ValueError("Installed skills path is not a directory")
    sources = read_sources(lock_file)
    records = []
    for skill in skills:
        expected = snapshot(skill)
        target = installed_dir / skill.name
        exists = target.exists()
        actual = snapshot(target) if exists else {}
        source = sources.get(skill.name, {}).get("source", "")
        name = source_name(source) if source else "unknown"
        records.append({
            "skill": skill.name,
            "content": "missing" if not exists else "match" if actual == expected else "different",
            "source": name,
            "provenance": "unknown" if not source else "match" if name == EXPECTED_SOURCE else "different",
            "missing": sorted(expected.keys() - actual.keys()),
            "changed": sorted(k for k in expected.keys() & actual.keys() if expected[k] != actual[k]),
            "extra": sorted(actual.keys() - expected.keys()),
        })
    return {"expected_source": EXPECTED_SOURCE, "skills": records}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, default=Path(__file__).resolve().parents[1] / "skills")
    parser.add_argument("--installed-dir", type=Path, default=Path.home() / ".agents" / "skills")
    parser.add_argument("--lock-file", type=Path, help="Defaults to .skill-lock.json beside the installed skills directory")
    parser.add_argument("--json", action="store_true", help="Print structured results instead of a text report")
    args = parser.parse_args()
    try:
        report = compare(args.source_dir, args.installed_dir,
                         args.lock_file or args.installed_dir.parent / ".skill-lock.json")
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Expected source: {report['expected_source']}")
        for record in report["skills"]:
            print(f"{record['skill']}: content={record['content']}; "
                  f"source={record['source']}; provenance={record['provenance']}")
            for field in ("missing", "changed", "extra"):
                if record[field]:
                    print(f"  {field}: {', '.join(record[field])}")
    return int(any(r["content"] != "match" or r["provenance"] != "match" for r in report["skills"]))


if __name__ == "__main__":
    raise SystemExit(main())
