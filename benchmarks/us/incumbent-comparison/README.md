# US Incumbent Comparison

This directory owns the US incumbent replacement benchmark for Microcosm-US.
It is outside the live Microcosm repo so release code does not carry historical
comparison harnesses or local-baseline assumptions.

## Required Inputs

- Candidate Microcosm-US HDF5 artifact.
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
