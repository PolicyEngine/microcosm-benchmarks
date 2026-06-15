# US Incumbent Comparison

This directory owns the US incumbent replacement benchmark for Populace-US.
It is outside the live Populace repo so release code does not carry historical
comparison harnesses or local-baseline assumptions.

## Required Inputs

- Candidate Populace-US HDF5 artifact.
- Certified pinned production incumbent HDF5 artifact from the manifest.
- Frozen benchmark target manifest used for the replacement decision.
- Explicit output directory for scorecards and diagnostics.

## Non-Goals

- Building a candidate artifact.
- Publishing a population dataset.
- Running development or local-baseline scorecards as promotion evidence.

## Promotion Metrics

The benchmark must report at least:

- full target loss
- holdout target loss
- unweighted mean squared relative error
- target-level win/loss/tie counts
- support, export, and lineage gate status

Promotion requires wins on full loss, holdout loss, and unweighted MSRE, plus
green export/support/lineage gates. A result that wins an aggregate flag but
loses any required promotion metric is not promotion-valid.

## Baseline Rules

Use only the pinned production incumbent recorded in
`manifests/pinned-production-ecps-2024.json` for promotion comparisons. Known
local or development copies of the incumbent are not equivalent, even when they
share a similar file name.

## Published Scorecards

Each comparison run publishes a machine-readable scorecard so consumers (the
[calibration-diagnostics dashboard](https://github.com/PolicyEngine/calibration-diagnostics))
can read the head-to-head without re-running the harness:

- **Scorecard** — `archive/us/<candidate-build-id>/scorecard.json`, conforming
  to [`scorecard.schema.json`](scorecard.schema.json). It carries the promotion
  metrics (full / holdout loss, unweighted MSRE), per-target win/loss/tie,
  per-family loss breakdown, and the top movers.
- **Pointer** — [`latest.json`](latest.json) names the most recent scorecard
  (`scorecard_path` + `candidate_release_id`), so a consumer resolves the
  current scorecard without hard-coding a path.

A scorecard's `status` is `archived` when it was recomputed from a historical
candidate's published comparison (rather than a fresh benchmark run against the
pinned incumbent HDF5s). The first published scorecard,
`populace-us-2024-9f1260b-20260611`, is archived: it was reconstructed from that
release's `sound_ecps_replacement_comparison.json` on the populace-us dataset.

### Validation

`tools/validate_scorecard.py` (stdlib only) checks every scorecard and pointer —
required keys, promotion-metric types, and internal consistency the schema
cannot express (win counts sum to the target count; `candidate_beats_baseline`
agrees with the loss values). It runs in CI on every PR
(`.github/workflows/validate-scorecards.yml`) and locally:

```bash
python tools/validate_scorecard.py
```
