#!/usr/bin/env python3
"""Validate the closed Boluobao v1 skill package using only the standard library."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import struct
import sys
from collections import defaultdict
from pathlib import Path


FORBIDDEN_DIRECTORY_TOKENS = ("working", "candidate")
REPOSITORY_METADATA_DIRECTORIES = {".git", "__pycache__"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    return struct.unpack(">II", header[16:24])


def webp_size(path: Path) -> tuple[int, int]:
    """Read dimensions from VP8, VP8L, or VP8X WebP data."""
    data = path.read_bytes()
    if len(data) < 20 or data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        raise ValueError("not a WebP file")
    offset = 12
    while offset + 8 <= len(data):
        chunk_type = data[offset : offset + 4]
        chunk_size = int.from_bytes(data[offset + 4 : offset + 8], "little")
        payload = data[offset + 8 : offset + 8 + chunk_size]
        if chunk_type == b"VP8X" and len(payload) >= 10:
            width = int.from_bytes(payload[4:7], "little") + 1
            height = int.from_bytes(payload[7:10], "little") + 1
            return width, height
        if chunk_type == b"VP8L" and len(payload) >= 5 and payload[0] == 0x2F:
            bits = int.from_bytes(payload[1:5], "little")
            return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
        if chunk_type == b"VP8 " and len(payload) >= 10 and payload[3:6] == b"\x9d\x01\x2a":
            width = int.from_bytes(payload[6:8], "little") & 0x3FFF
            height = int.from_bytes(payload[8:10], "little") & 0x3FFF
            return width, height
        offset += 8 + chunk_size + (chunk_size % 2)
    raise ValueError("unsupported WebP dimensions")


def ratio_value(label: str) -> float:
    match = re.fullmatch(r"([0-9]+(?:\.[0-9]+)?):([0-9]+(?:\.[0-9]+)?)", label)
    if not match:
        raise ValueError(f"invalid ratio label: {label}")
    return float(match.group(1)) / float(match.group(2))


def relative_links(markdown: Path) -> list[Path]:
    text = markdown.read_text(encoding="utf-8")
    links = []
    for raw in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = raw.strip().split("#", 1)[0]
        if not target or re.match(r"^[a-z]+://", target, re.I):
            continue
        links.append((markdown.parent / target).resolve())
    return links


def package_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative_parts = path.relative_to(root).parts
        if any(part in REPOSITORY_METADATA_DIRECTORIES for part in relative_parts):
            continue
        files.append(path)
    return files


def validate(root: Path) -> list[str]:
    failures: list[str] = []
    root = root.resolve()
    skill_md = root / "SKILL.md"
    readme = root / "README.md"
    apache_license = root / "LICENSE"
    cc_license = root / "LICENSES" / "CC-BY-4.0.txt"
    asset_terms = root / "ASSETS-LICENSE.md"
    notice = root / "NOTICE"
    openai_yaml = root / "agents" / "openai.yaml"
    claude_bridge = root / ".claude" / "skills" / "boluobao" / "SKILL.md"
    claude_sync = root / "scripts" / "sync_claude_skill.py"
    manifest_path = root / "assets" / "tests" / "test-manifest.json"
    invocation_path = root / "assets" / "tests" / "invocation-cases.json"

    if not skill_md.is_file():
        return ["missing SKILL.md"]
    skill_text = skill_md.read_text(encoding="utf-8")
    if not skill_text.startswith("---\n") or "\n---\n" not in skill_text[4:]:
        failures.append("SKILL.md frontmatter is missing or malformed")
    if not re.search(r"(?m)^name:\s*boluobao\s*$", skill_text):
        failures.append("SKILL.md name must remain boluobao")
    if not re.search(r"(?m)^description:\s*.+$", skill_text):
        failures.append("SKILL.md description is missing")

    markdown_files = [skill_md, *sorted((root / "references").glob("*.md"))]
    if readme.is_file():
        markdown_files.append(readme)
    else:
        failures.append("missing GitHub README.md")
    for markdown in markdown_files:
        for target in relative_links(markdown):
            if not target.exists():
                failures.append(f"broken Markdown link in {markdown.relative_to(root)}: {target}")

    if not apache_license.is_file():
        failures.append("missing root Apache-2.0 LICENSE")
    else:
        license_text = apache_license.read_text(encoding="utf-8")
        apache_fragments = [
            "Apache License",
            "Version 2.0, January 2004",
            "Grant of Copyright License",
            "Grant of Patent License",
            "END OF TERMS AND CONDITIONS",
        ]
        for fragment in apache_fragments:
            if fragment not in license_text:
                failures.append(f"root LICENSE is missing Apache-2.0 text: {fragment}")

    if not cc_license.is_file():
        failures.append("missing LICENSES/CC-BY-4.0.txt")
    else:
        cc_text = cc_license.read_text(encoding="utf-8")
        for fragment in (
            "Creative Commons Attribution 4.0 International Public License",
            "Section 5 -- Disclaimer of Warranties and Limitation of Liability",
            "Section 6 -- Term and Termination",
        ):
            if fragment not in cc_text:
                failures.append(f"CC BY 4.0 license text is missing: {fragment}")

    if not asset_terms.is_file():
        failures.append("missing ASSETS-LICENSE.md")
    else:
        terms_text = asset_terms.read_text(encoding="utf-8")
        required_scopes = [
            "assets/tests/",
            "assets/brand/",
            "docs/showcase/",
            "assets/references/",
            "Apache-2.0",
            "CC BY 4.0",
            "all rights reserved",
            "no license granted",
        ]
        for scope in required_scopes:
            if scope not in terms_text:
                failures.append(f"ASSETS-LICENSE.md is missing scope: {scope}")

    if not notice.is_file():
        failures.append("missing NOTICE")

    if not openai_yaml.is_file():
        failures.append("missing agents/openai.yaml")
    else:
        yaml_text = openai_yaml.read_text(encoding="utf-8")
        required_fragments = [
            'icon_small: "./assets/brand/boluobao-icon-400.png"',
            'icon_large: "./assets/brand/boluobao-icon-1024.png"',
            'brand_color: "#D47B3B"',
            "allow_implicit_invocation: true",
            "$boluobao",
        ]
        for fragment in required_fragments:
            if fragment not in yaml_text:
                failures.append(f"agents/openai.yaml missing: {fragment}")

    if not claude_bridge.is_file():
        failures.append("missing Claude Code project bridge")
    else:
        bridge_text = claude_bridge.read_text(encoding="utf-8")
        required_fragments = [
            "name: boluobao",
            "../../../SKILL.md",
            "/boluobao",
            "agents/openai.yaml",
        ]
        for fragment in required_fragments:
            if fragment not in bridge_text:
                failures.append(f"Claude Code bridge missing: {fragment}")

    if not claude_sync.is_file():
        failures.append("missing Claude Code synchronization script")
    else:
        sync_text = claude_sync.read_text(encoding="utf-8")
        required_fragments = [
            'Path.home() / ".claude" / "skills" / "boluobao"',
            'Path("assets/references")',
            'Path("assets/tests")',
            'Path("assets/brand")',
            "SYNC_MANIFEST",
        ]
        for fragment in required_fragments:
            if fragment not in sync_text:
                failures.append(f"Claude Code synchronizer missing: {fragment}")

    if not manifest_path.is_file():
        failures.append("missing assets/tests/test-manifest.json")
        return failures

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"invalid test manifest: {exc}")
        return failures

    if manifest.get("schema_version") != 1:
        failures.append("test manifest schema_version must be 1")
    if manifest.get("package_version") != "1.2.0":
        failures.append("test manifest package_version must be 1.2.0")
    style_references = manifest.get("style_references", [])
    samples = manifest.get("samples", [])
    if len(style_references) != 8:
        failures.append(f"expected 8 style references, found {len(style_references)}")
    if len(samples) != 21:
        failures.append(f"expected 21 retained test samples, found {len(samples)}")

    for relative in [*style_references, *manifest.get("support_files", [])]:
        if not (root / relative).is_file():
            failures.append(f"missing manifest resource: {relative}")

    showcase_files = manifest.get("showcase_files", [])
    if len(showcase_files) != 12:
        failures.append(f"expected 12 GitHub showcase images, found {len(showcase_files)}")
    expected_showcase_layout = {
        "case_studies": {"count": 8, "width": 720, "height": 900, "ratio_label": "4:5"},
        "capability_boards": {
            "count": 4,
            "width": 1200,
            "height": 675,
            "ratio_label": "16:9",
        },
    }
    showcase_layout = manifest.get("showcase_layout", {})
    if showcase_layout != expected_showcase_layout:
        failures.append("showcase_layout must define 8 aligned 4:5 cases and 4 aligned 16:9 boards")
    readme_text = readme.read_text(encoding="utf-8") if readme.is_file() else ""
    for fragment in (
        "~/.claude/skills/boluobao/",
        "scripts/sync_claude_skill.py --install-user",
        "/boluobao",
    ):
        if fragment not in readme_text:
            failures.append(f"README.md missing Claude Code usage: {fragment}")

    expected_project_hero = {
        "file": "docs/showcase/boluobao-hero-16x9.webp",
        "width": 1200,
        "height": 675,
        "ratio_label": "16:9",
        "max_bytes": 150 * 1024,
    }
    project_hero = manifest.get("project_hero", {})
    if project_hero != expected_project_hero:
        failures.append("project_hero must define the verified 1200x675 GitHub cover")
    else:
        hero_relative = project_hero["file"]
        hero_path = root / hero_relative
        if not hero_path.is_file():
            failures.append(f"missing project hero: {hero_relative}")
        else:
            if hero_path.suffix.lower() != ".webp":
                failures.append(f"project hero must be WebP: {hero_relative}")
            if hero_relative.replace("\\", "/") not in readme_text:
                failures.append(f"project hero is not displayed in README.md: {hero_relative}")
            if hero_path.stat().st_size > project_hero["max_bytes"]:
                failures.append(f"project hero exceeds 150 KB: {hero_relative}")
            try:
                hero_width, hero_height = webp_size(hero_path)
            except ValueError as exc:
                failures.append(f"cannot read project hero dimensions for {hero_relative}: {exc}")
            else:
                if (hero_width, hero_height) != (project_hero["width"], project_hero["height"]):
                    failures.append(
                        f"{hero_relative}: dimensions {hero_width}x{hero_height}, expected "
                        f"{project_hero['width']}x{project_hero['height']} for project_hero"
                    )

    expected_cover_variants = [
        {
            "file": "docs/showcase/cover-x-5x2-v1.webp",
            "platform": "x",
            "width": 1500,
            "height": 600,
            "ratio_label": "5:2",
            "max_bytes": 150 * 1024,
        }
    ]
    cover_variants = manifest.get("project_cover_variants", [])
    if cover_variants != expected_cover_variants:
        failures.append("project_cover_variants must define the verified 1500x600 X cover")
    else:
        for cover in cover_variants:
            cover_relative = cover["file"]
            cover_path = root / cover_relative
            if not cover_path.is_file():
                failures.append(f"missing project cover variant: {cover_relative}")
                continue
            if cover_path.suffix.lower() != ".webp":
                failures.append(f"project cover variant must be WebP: {cover_relative}")
            if cover_relative.replace("\\", "/") not in readme_text:
                failures.append(f"project cover variant is not linked in README.md: {cover_relative}")
            if cover_path.stat().st_size > cover["max_bytes"]:
                failures.append(f"project cover variant exceeds 150 KB: {cover_relative}")
            try:
                cover_width, cover_height = webp_size(cover_path)
            except ValueError as exc:
                failures.append(f"cannot read project cover dimensions for {cover_relative}: {exc}")
            else:
                if (cover_width, cover_height) != (cover["width"], cover["height"]):
                    failures.append(
                        f"{cover_relative}: dimensions {cover_width}x{cover_height}, expected "
                        f"{cover['width']}x{cover['height']} for {cover['platform']}"
                    )

    showcase_bytes = 0
    for relative in showcase_files:
        path = root / relative
        if not path.is_file():
            failures.append(f"missing showcase image: {relative}")
            continue
        if path.suffix.lower() != ".webp":
            failures.append(f"showcase image must be WebP: {relative}")
        if relative.replace("\\", "/") not in readme_text:
            failures.append(f"showcase image is not displayed in README.md: {relative}")
        if path.stat().st_size > 150 * 1024:
            failures.append(f"showcase image exceeds 150 KB: {relative}")
        group = "capability_boards" if path.name.startswith("capability-") else "case_studies"
        expected = expected_showcase_layout[group]
        try:
            width, height = webp_size(path)
        except ValueError as exc:
            failures.append(f"cannot read showcase dimensions for {relative}: {exc}")
        else:
            if (width, height) != (expected["width"], expected["height"]):
                failures.append(
                    f"{relative}: dimensions {width}x{height}, expected "
                    f"{expected['width']}x{expected['height']} for {group}"
                )
        showcase_bytes += path.stat().st_size
    if showcase_bytes > 1024 * 1024:
        failures.append("GitHub showcase images exceed 1 MB total")

    if not invocation_path.is_file():
        failures.append("missing assets/tests/invocation-cases.json")
    else:
        try:
            invocation = json.loads(invocation_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            failures.append(f"invalid invocation cases: {exc}")
        else:
            if invocation.get("schema_version") != 1:
                failures.append("invocation cases schema_version must be 1")
            cases = invocation.get("cases", [])
            expected_case_ids = {
                "single-paragraph-article",
                "multi-paragraph-article",
                "generic-social-cover",
                "platform-cover-set",
                "image-style-reconstruction",
                "data-bar-chart",
                "compact-data-table",
            }
            case_ids = {case.get("id") for case in cases}
            if len(cases) != 7 or case_ids != expected_case_ids:
                failures.append("invocation cases must contain the seven v1.1 routing scenarios")
            case_by_id = {case.get("id"): case for case in cases}
            generic = case_by_id.get("generic-social-cover", {})
            if generic.get("expected_ratio") != "4:5":
                failures.append("generic social cover fallback must be 4:5")
            single = case_by_id.get("single-paragraph-article", {})
            if single.get("expected_count") != 1 or single.get("expected_ratio") != "16:9":
                failures.append("single-paragraph article must route to one 16:9 image")
            multi = case_by_id.get("multi-paragraph-article", {})
            if multi.get("expected_count_min") != 2 or multi.get("expected_count_max") != 3:
                failures.append("multi-paragraph article must route to two or three images")
            chart = case_by_id.get("data-bar-chart", {})
            if chart.get("expected_mode") != "data-chart" or chart.get("expected_ratio") != "16:9":
                failures.append("bar-chart request must route to one 16:9 data chart")
            table = case_by_id.get("compact-data-table", {})
            if table.get("expected_mode") != "data-table" or table.get("expected_ratio") != "16:9":
                failures.append("table request must route to one 16:9 compact data table")
            policy = invocation.get("exact_text_policy", {})
            if policy.get("maximum_surgical_corrections") != 1:
                failures.append("exact-text policy must allow exactly one surgical correction")
            if any(
                policy.get(key) != "blank-fallback"
                for key in ("cover_or_article_second_failure", "letter_second_failure")
            ):
                failures.append("second exact-text failure must route to blank-fallback")
            if policy.get("protected_data_second_failure") != "fail":
                failures.append("second protected-data failure must fail the data graphic")
            regression = invocation.get("exact_text_regression", {})
            if regression.get("expected") == regression.get("first_generated"):
                failures.append("exact-text regression fixture must contain a wrong first output")
            if regression.get("first_action") != "surgical-correction":
                failures.append("first exact-text failure must request surgical-correction")
            if regression.get("second_action") != "blank-fallback":
                failures.append("second exact-text failure must request blank-fallback")
            if regression.get("final_exact_text_status") != "blank-fallback":
                failures.append("exact-text regression fixture must end as blank-fallback")
            retention = invocation.get("retention_policy", {})
            expected_retention = {
                "default": "final-only",
                "scope": "active-request",
                "rejected_candidates": "do-not-copy-to-project-output",
                "superseded_corrections": "do-not-deliver",
                "requested_multi-image_set": "retain-each-accepted-deliverable",
                "dedicated_task_staging": "cleanup-after-verified-final-copy",
                "shared_generator_cache": "never-recursively-delete",
                "previously_delivered_tasks": "preserve",
            }
            if any(retention.get(key) != value for key, value in expected_retention.items()):
                failures.append("retention policy must enforce final-only active-request delivery")
            required_delivery = {
                "source_role",
                "visual_proposition",
                "anchor_state",
                "ratio",
                "pixel_dimensions",
                "exact_text_status",
                "data_verification_status",
                "rubric_score",
                "absolute_path",
            }
            if not required_delivery.issubset(set(invocation.get("delivery_fields", []))):
                failures.append("invocation delivery_fields are incomplete")

    for sample in samples:
        relative = sample.get("file", "")
        path = root / relative
        if not path.is_file():
            failures.append(f"missing test sample: {relative}")
            continue
        try:
            width, height = png_size(path)
        except ValueError as exc:
            failures.append(f"{relative}: {exc}")
            continue
        if width != sample.get("width") or height != sample.get("height"):
            failures.append(
                f"{relative}: dimensions {width}x{height}, expected "
                f"{sample.get('width')}x{sample.get('height')}"
            )
        try:
            expected_ratio = ratio_value(sample.get("ratio_label", ""))
            actual_ratio = width / height
            if abs(actual_ratio - expected_ratio) > 0.01:
                failures.append(
                    f"{relative}: ratio {actual_ratio:.4f} outside tolerance for "
                    f"{sample.get('ratio_label')}"
                )
        except ValueError as exc:
            failures.append(f"{relative}: {exc}")
        expected_hash = sample.get("sha256", "").upper()
        if expected_hash and sha256(path) != expected_hash:
            failures.append(f"{relative}: SHA-256 does not match the approved sample")
        role = sample.get("quality_role")
        score = sample.get("score", 0)
        if role == "gold" and score < 19:
            failures.append(f"{relative}: gold sample must score at least 19")
        if role == "baseline" and score < 18:
            failures.append(f"{relative}: baseline sample must score at least 18")

    icon_expectations = {
        root / "assets" / "brand" / "boluobao-icon-400.png": (400, 400),
        root / "assets" / "brand" / "boluobao-icon-1024.png": (1024, 1024),
    }
    for icon, expected in icon_expectations.items():
        if icon.is_file():
            try:
                if png_size(icon) != expected:
                    failures.append(
                        f"{icon.relative_to(root)} must be {expected[0]}x{expected[1]}"
                    )
            except ValueError as exc:
                failures.append(f"{icon.relative_to(root)}: {exc}")

    for directory in [p for p in root.rglob("*") if p.is_dir()]:
        name = directory.name.lower()
        if name == "output" or any(token in name for token in FORBIDDEN_DIRECTORY_TOKENS):
            failures.append(f"forbidden package directory: {directory.relative_to(root)}")

    hash_paths: dict[str, list[Path]] = defaultdict(list)
    for image in sorted((root / "assets").rglob("*")):
        if image.is_file() and image.suffix.lower() in {".png", ".jpg", ".jpeg"}:
            hash_paths[sha256(image)].append(image)
    for paths in hash_paths.values():
        if len(paths) > 1:
            joined = ", ".join(str(path.relative_to(root)) for path in paths)
            failures.append(f"duplicate image content: {joined}")

    package_bytes = sum(path.stat().st_size for path in package_files(root))
    max_package_mb = float(manifest.get("max_package_mb", 60))
    package_mb = package_bytes / (1024 * 1024)
    if package_mb > max_package_mb:
        failures.append(
            f"package size {package_mb:.1f} MB exceeds {max_package_mb:.1f} MB"
        )

    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Boluobao skill root",
    )
    args = parser.parse_args()
    failures = validate(args.root)
    if failures:
        print("Boluobao package validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    root = args.root.resolve()
    size_mb = sum(path.stat().st_size for path in package_files(root)) / (
        1024 * 1024
    )
    print(f"Boluobao package valid: {size_mb:.1f} MB, 21 samples, 8 references")
    return 0


if __name__ == "__main__":
    sys.exit(main())
