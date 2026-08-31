#!/usr/bin/env python3
"""Synchronize the canonical Boluobao package into a Claude Code skill folder."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SYNC_MANIFEST = ".boluobao-claude-sync.json"
SYNC_SCHEMA_VERSION = 1
SYNC_ENTRIES = (
    Path("SKILL.md"),
    Path("references"),
    Path("assets/references"),
    Path("assets/tests"),
    Path("assets/brand"),
    Path("LICENSE"),
    Path("LICENSES"),
    Path("NOTICE"),
    Path("ASSETS-LICENSE.md"),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def source_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for relative in SYNC_ENTRIES:
        source = root / relative
        if source.is_file():
            files.append(source)
        elif source.is_dir():
            files.extend(path for path in source.rglob("*") if path.is_file())
        else:
            raise FileNotFoundError(f"missing canonical source entry: {relative.as_posix()}")
    return sorted(files, key=lambda path: path.relative_to(root).as_posix())


def package_version(root: Path) -> str:
    manifest = root / "assets" / "tests" / "test-manifest.json"
    data = json.loads(manifest.read_text(encoding="utf-8"))
    return str(data["package_version"])


def source_inventory(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): sha256(path)
        for path in source_files(root)
    }


def installed_manifest(target: Path) -> dict[str, object] | None:
    marker = target / SYNC_MANIFEST
    if not marker.is_file():
        return None
    data = json.loads(marker.read_text(encoding="utf-8"))
    if data.get("schema_version") != SYNC_SCHEMA_VERSION or data.get("skill") != "boluobao":
        raise ValueError(f"unrecognized sync manifest: {marker}")
    return data


def validate_target(target: Path) -> Path:
    resolved = target.expanduser().resolve()
    repository = REPOSITORY_ROOT.resolve()
    home = Path.home().resolve()
    if resolved.name.casefold() != "boluobao":
        raise ValueError("target directory must be named 'boluobao'")
    if resolved == repository or repository in resolved.parents:
        raise ValueError("target must be outside the repository to avoid duplicating the 60 MB package")
    if resolved in {home, home / ".claude", home / ".claude" / "skills"}:
        raise ValueError("target must be the dedicated ~/.claude/skills/boluobao directory")
    return resolved


def remove_stale_managed_files(target: Path, old_files: set[str], new_files: set[str]) -> None:
    for relative in sorted(old_files - new_files, reverse=True):
        candidate = (target / relative).resolve()
        if target not in candidate.parents:
            raise ValueError(f"unsafe managed path in sync manifest: {relative}")
        if candidate.is_file():
            candidate.unlink()


def write_manifest(target: Path, inventory: dict[str, str]) -> None:
    data = {
        "schema_version": SYNC_SCHEMA_VERSION,
        "skill": "boluobao",
        "package_version": package_version(REPOSITORY_ROOT),
        "source": "canonical Boluobao repository",
        "files": inventory,
    }
    marker = target / SYNC_MANIFEST
    temporary = marker.with_suffix(".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(marker)


def sync(target: Path, dry_run: bool = False) -> int:
    inventory = source_inventory(REPOSITORY_ROOT)
    total_bytes = sum((REPOSITORY_ROOT / relative).stat().st_size for relative in inventory)
    if dry_run:
        print(
            f"Claude Code sync plan: {len(inventory)} files, "
            f"{total_bytes / (1024 * 1024):.1f} MB -> {target}"
        )
        return 0

    prior = installed_manifest(target) if target.exists() else None
    if target.exists() and any(target.iterdir()) and prior is None:
        raise ValueError(
            f"refusing to overwrite unmanaged non-empty directory: {target}. "
            "Move it aside or choose a new target."
        )

    target.mkdir(parents=True, exist_ok=True)
    old_files = set(prior.get("files", {})) if prior else set()
    remove_stale_managed_files(target, old_files, set(inventory))

    for relative in inventory:
        source = REPOSITORY_ROOT / relative
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    write_manifest(target, inventory)
    print(
        f"Boluobao {package_version(REPOSITORY_ROOT)} synchronized for Claude Code: "
        f"{len(inventory)} files, {total_bytes / (1024 * 1024):.1f} MB -> {target}"
    )
    return 0


def check(target: Path) -> int:
    if not target.is_dir():
        print(f"Claude Code skill is not installed: {target}", file=sys.stderr)
        return 1
    prior = installed_manifest(target)
    if prior is None:
        print(f"Claude Code skill is not managed by this synchronizer: {target}", file=sys.stderr)
        return 1

    expected = source_inventory(REPOSITORY_ROOT)
    recorded = prior.get("files", {})
    failures: list[str] = []
    if prior.get("package_version") != package_version(REPOSITORY_ROOT):
        failures.append("installed package version differs from the canonical package")
    if recorded != expected:
        failures.append("source inventory changed after the last sync")
    for relative, expected_hash in expected.items():
        installed = target / relative
        if not installed.is_file():
            failures.append(f"missing installed file: {relative}")
        elif sha256(installed) != expected_hash:
            failures.append(f"modified installed file: {relative}")

    if failures:
        print("Claude Code sync check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(
        f"Claude Code skill is synchronized: Boluobao {package_version(REPOSITORY_ROOT)}, "
        f"{len(expected)} files -> {target}"
    )
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync the canonical Boluobao package to a Claude Code skill directory."
    )
    destination = parser.add_mutually_exclusive_group(required=True)
    destination.add_argument(
        "--install-user",
        action="store_true",
        help="target ~/.claude/skills/boluobao",
    )
    destination.add_argument(
        "--target",
        type=Path,
        help="target a dedicated directory named boluobao outside this repository",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify that the target matches the current canonical package",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="show file count, size, and destination without writing",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    raw_target = Path.home() / ".claude" / "skills" / "boluobao" if args.install_user else args.target
    try:
        target = validate_target(raw_target)
        if args.check:
            if args.dry_run:
                raise ValueError("--check and --dry-run cannot be used together")
            return check(target)
        return sync(target, dry_run=args.dry_run)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"Claude Code synchronization failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
