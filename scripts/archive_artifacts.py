#!/usr/bin/env python3
"""Safely archive non-package Boluobao artifacts with a recoverable hash manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def safe_roots(source: Path, archive: Path) -> tuple[Path, Path]:
    source = source.resolve()
    archive = archive.resolve()
    if not (source / "SKILL.md").is_file():
        raise ValueError(f"source is not a skill root: {source}")
    if source == archive or source in archive.parents:
        raise ValueError("archive must be outside the skill root")
    expected_container = source.parent / f"{source.name}-archive"
    if archive.parent != expected_container:
        raise ValueError(
            f"archive must be a dated child of the sibling container: {expected_container}"
        )
    return source, archive


def retained_files(source: Path) -> set[Path]:
    manifest_path = source / "assets" / "tests" / "test-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    keep = {
        Path("SKILL.md"),
        Path("assets/tests/test-manifest.json"),
    }
    keep.update(Path(item) for item in manifest.get("style_references", []))
    keep.update(Path(item) for item in manifest.get("support_files", []))
    keep.update(Path(item["file"]) for item in manifest.get("samples", []))
    for folder in ("agents", "references", "scripts", "assets/brand"):
        base = source / folder
        if base.exists():
            keep.update(path.relative_to(source) for path in base.rglob("*") if path.is_file())
    return keep


def archive_candidates(source: Path, keep: set[Path]) -> list[Path]:
    candidates = []
    for path in source.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(source)
        if relative.parts[0].lower() == "output":
            candidates.append(path)
        elif relative.parts[0].lower() == "assets" and relative not in keep:
            candidates.append(path)
    return sorted(candidates)


def build_manifest(source: Path, archive: Path, candidates: list[Path]) -> dict:
    entries = []
    for path in candidates:
        relative = path.relative_to(source)
        entries.append(
            {
                "relative_path": relative.as_posix(),
                "destination_path": (archive / relative).as_posix(),
                "size": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    return {
        "schema_version": 1,
        "status": "planned",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_root": str(source),
        "archive_root": str(archive),
        "file_count": len(entries),
        "total_bytes": sum(entry["size"] for entry in entries),
        "entries": entries,
    }


def remove_empty_directories(source: Path) -> None:
    directories = sorted(
        (path for path in source.rglob("*") if path.is_dir()),
        key=lambda path: len(path.parts),
        reverse=True,
    )
    for directory in directories:
        try:
            directory.rmdir()
        except OSError:
            pass


def execute_archive(source: Path, archive: Path, manifest: dict) -> None:
    if archive.exists() and any(archive.iterdir()):
        raise ValueError(f"archive destination is not empty: {archive}")
    archive.mkdir(parents=True, exist_ok=True)
    source_manifest = source / "archive-manifest-2026-08-31.json"
    source_manifest.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    archive_manifest = archive / "archive-manifest.json"
    shutil.move(str(source_manifest), str(archive_manifest))

    for entry in manifest["entries"]:
        source_path = source / Path(entry["relative_path"])
        destination = archive / Path(entry["relative_path"])
        if not source_path.is_file():
            raise FileNotFoundError(f"source disappeared before move: {source_path}")
        if destination.exists():
            raise FileExistsError(f"archive collision: {destination}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(source_path), str(destination))
        if sha256(destination) != entry["sha256"]:
            raise IOError(f"hash verification failed after move: {destination}")

    remove_empty_directories(source)
    manifest["status"] = "completed"
    manifest["completed_at_utc"] = datetime.now(timezone.utc).isoformat()
    archive_manifest.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("archive", type=Path)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--dry-run", action="store_true")
    action.add_argument("--execute", action="store_true")
    args = parser.parse_args()

    try:
        source, archive = safe_roots(args.source, args.archive)
        keep = retained_files(source)
        candidates = archive_candidates(source, keep)
        manifest = build_manifest(source, archive, candidates)
        print(
            f"source={source}\narchive={archive}\n"
            f"files={manifest['file_count']}\n"
            f"megabytes={manifest['total_bytes'] / (1024 * 1024):.1f}"
        )
        for entry in manifest["entries"]:
            print(entry["relative_path"])
        if args.execute:
            execute_archive(source, archive, manifest)
            print(f"archive completed: {archive / 'archive-manifest.json'}")
        return 0
    except Exception as exc:
        print(f"archive failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
