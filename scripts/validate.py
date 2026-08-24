#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FORBIDDEN_PROJECT_DIRS = (".agents", ".cursor", ".claude", ".opencode")


def parse_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening YAML frontmatter delimiter")

    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("missing closing YAML frontmatter delimiter") from exc

    values: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip("\"'")

    if not any(line.strip() for line in lines[end + 1 :]):
        raise ValueError("skill body is empty")
    return values


def local_markdown_links(path: Path) -> list[Path]:
    links: list[Path] = []
    for target in LINK_PATTERN.findall(path.read_text(encoding="utf-8")):
        target = target.strip().strip("<>").split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        links.append((path.parent / target).resolve())
    return links


def main() -> int:
    errors: list[str] = []

    if not SKILLS_DIR.is_dir():
        errors.append("skills/ directory is missing")
        skill_dirs: list[Path] = []
    else:
        skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    notices = (ROOT / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8")

    for directory in skill_dirs:
        skill_file = directory / "SKILL.md"
        if not NAME_PATTERN.fullmatch(directory.name):
            errors.append(f"{directory.relative_to(ROOT)} has an invalid skill directory name")
        if not skill_file.is_file():
            errors.append(f"{directory.relative_to(ROOT)} is missing SKILL.md")
            continue

        try:
            frontmatter = parse_frontmatter(skill_file)
        except ValueError as exc:
            errors.append(f"{skill_file.relative_to(ROOT)}: {exc}")
            continue

        if frontmatter.get("name") != directory.name:
            errors.append(
                f"{skill_file.relative_to(ROOT)} name must match directory {directory.name!r}"
            )
        if not frontmatter.get("description"):
            errors.append(f"{skill_file.relative_to(ROOT)} is missing a description")
        if f"skills/{directory.name}/SKILL.md" not in readme:
            errors.append(f"README.md does not catalog {directory.name}")

    for directory_name in FORBIDDEN_PROJECT_DIRS:
        if (ROOT / directory_name).exists():
            errors.append(f"{directory_name}/ must not be committed; DST Stack installs globally")

    if "46125561306434d8a1d7745d540d8932ab0cd2a2" not in notices:
        errors.append("THIRD_PARTY_NOTICES.md is missing the pinned pstack source")
    if "5b15a47f2d7150f545fbcacbfe381787fc0230dc" not in notices:
        errors.append("THIRD_PARTY_NOTICES.md is missing the pinned Matt Pocock source")
    if "skills/engineering/research/SKILL.md" not in notices:
        errors.append("THIRD_PARTY_NOTICES.md is missing the Matt Pocock research source")
    if "skills/engineering/prototype/SKILL.md" not in notices:
        errors.append("THIRD_PARTY_NOTICES.md is missing the Matt Pocock prototype source")
    if "skills/engineering/prototype/LOGIC.md" not in notices:
        errors.append("THIRD_PARTY_NOTICES.md is missing the Matt Pocock prototype logic source")
    if "skills/engineering/prototype/UI.md" not in notices:
        errors.append("THIRD_PARTY_NOTICES.md is missing the Matt Pocock prototype UI source")
    if "skills/engineering/code-review/SKILL.md" not in notices:
        errors.append("THIRD_PARTY_NOTICES.md is missing the Matt Pocock code-review source")
    if "skills/engineering/tdd/SKILL.md" not in notices:
        errors.append("THIRD_PARTY_NOTICES.md is missing the Matt Pocock TDD source")
    if "skills/engineering/tdd/tests.md" not in notices:
        errors.append("THIRD_PARTY_NOTICES.md is missing the Matt Pocock TDD tests source")
    if "skills/engineering/tdd/mocking.md" not in notices:
        errors.append("THIRD_PARTY_NOTICES.md is missing the Matt Pocock TDD mocking source")

    markdown_files = sorted(ROOT.glob("*.md"))
    if SKILLS_DIR.exists():
        markdown_files.extend(sorted(SKILLS_DIR.glob("**/*.md")))
    for markdown_file in markdown_files:
        for target in local_markdown_links(markdown_file):
            if not target.exists():
                errors.append(
                    f"{markdown_file.relative_to(ROOT)} has a broken local link to {target}"
                )

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
