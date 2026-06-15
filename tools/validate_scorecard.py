#!/usr/bin/env python3
"""Validate published incumbent-comparison scorecards (stdlib only).

A scorecard is the machine-readable result a candidate-vs-incumbent benchmark
run publishes (see ``benchmarks/us/incumbent-comparison/scorecard.schema.json``).
Consumers read it read-only, so a malformed or internally-inconsistent scorecard
is a published-contract break. This validator is the gate: it runs in CI on every
PR and is runnable locally with no dependencies.

It checks each scorecard for required keys and types, the promotion metrics, and
internal consistency the JSON Schema cannot express (win counts sum to the target
count). It also checks that every ``latest.json`` pointer resolves to a scorecard
that exists and whose ``candidate_release_id`` matches the pointer.

Usage:
    python tools/validate_scorecard.py            # validate everything tracked
    python tools/validate_scorecard.py PATH ...   # validate specific files
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_TOP = (
    "schema_version",
    "candidate_release_id",
    "incumbent_manifest",
    "baseline_label",
    "candidate_label",
    "summary",
)
# Promotion metrics (the benchmark manifest's required set) plus the win/tie
# counts the consistency check needs.
REQUIRED_SUMMARY_NUMERIC = (
    "candidate_loss",
    "baseline_loss",
    "candidate_holdout_loss",
    "baseline_holdout_loss",
    "candidate_unweighted_msre",
    "baseline_unweighted_msre",
)
REQUIRED_SUMMARY_COUNTS = ("candidate_wins", "baseline_wins", "ties", "n_targets")


def _is_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def validate_scorecard(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        return [f"{path}: invalid JSON: {exc}"]
    if not isinstance(data, dict):
        return [f"{path}: top level must be a JSON object"]

    for key in REQUIRED_TOP:
        if key not in data:
            errors.append(f"{path}: missing required key {key!r}")

    if data.get("schema_version") != 1:
        errors.append(
            f"{path}: schema_version must be 1, got {data.get('schema_version')!r}"
        )

    summary = data.get("summary")
    if not isinstance(summary, dict):
        errors.append(f"{path}: 'summary' must be an object")
        return errors

    for key in REQUIRED_SUMMARY_NUMERIC:
        if not _is_number(summary.get(key)):
            errors.append(f"{path}: summary.{key} must be a number")
    for key in REQUIRED_SUMMARY_COUNTS:
        value = summary.get(key)
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            errors.append(f"{path}: summary.{key} must be a non-negative integer")

    # Internal consistency the schema cannot express: the per-target verdicts
    # partition the scored targets exactly.
    counts = [summary.get(k) for k in ("candidate_wins", "baseline_wins", "ties")]
    n_targets = summary.get("n_targets")
    if all(isinstance(c, int) and not isinstance(c, bool) for c in counts) and isinstance(
        n_targets, int
    ):
        total = sum(counts)
        if total != n_targets:
            errors.append(
                f"{path}: candidate_wins + baseline_wins + ties = {total} "
                f"!= n_targets = {n_targets}"
            )

    # candidate_beats_baseline, when present, must agree with the loss sign.
    beats = summary.get("candidate_beats_baseline")
    if isinstance(beats, bool) and _is_number(summary.get("candidate_loss")) and _is_number(
        summary.get("baseline_loss")
    ):
        actual = summary["candidate_loss"] < summary["baseline_loss"]
        if beats != actual:
            errors.append(
                f"{path}: candidate_beats_baseline={beats} disagrees with the "
                f"loss values ({summary['candidate_loss']} vs "
                f"{summary['baseline_loss']})"
            )

    return errors


def validate_pointer(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        return [f"{path}: invalid JSON: {exc}"]

    scorecard_path = data.get("scorecard_path")
    if not isinstance(scorecard_path, str) or not scorecard_path:
        return [f"{path}: pointer missing 'scorecard_path'"]
    target = REPO_ROOT / scorecard_path
    if not target.is_file():
        return [f"{path}: scorecard_path {scorecard_path!r} does not exist"]

    errors.extend(validate_scorecard(target))
    pointer_release = data.get("candidate_release_id")
    scorecard_release = json.loads(target.read_text()).get("candidate_release_id")
    if pointer_release != scorecard_release:
        errors.append(
            f"{path}: pointer candidate_release_id {pointer_release!r} != "
            f"scorecard {scorecard_release!r}"
        )
    return errors


def discover() -> tuple[list[Path], list[Path]]:
    scorecards = sorted((REPO_ROOT / "archive").rglob("scorecard.json"))
    pointers = sorted((REPO_ROOT / "benchmarks").rglob("latest.json"))
    return scorecards, pointers


def main(argv: list[str]) -> int:
    if argv:
        scorecards = [Path(a) for a in argv if Path(a).name != "latest.json"]
        pointers = [Path(a) for a in argv if Path(a).name == "latest.json"]
    else:
        scorecards, pointers = discover()

    errors: list[str] = []
    for path in scorecards:
        errors.extend(validate_scorecard(path))
    for path in pointers:
        errors.extend(validate_pointer(path))

    checked = len(scorecards) + len(pointers)
    if errors:
        print(f"FAIL: {len(errors)} problem(s) across {checked} file(s):")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"OK: {checked} file(s) valid ({len(scorecards)} scorecard(s), "
          f"{len(pointers)} pointer(s)).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
