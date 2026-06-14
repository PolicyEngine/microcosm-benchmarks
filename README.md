# populace-benchmarks

External benchmark harnesses and archived incumbent comparisons for Populace.

This repository is intentionally separate from
[`PolicyEngine/populace`](https://github.com/PolicyEngine/populace). The live
Populace repo owns the library code, build contracts, package tests, release
gates, and published population registry. Incumbent replacement comparisons,
historical candidate scorecards, and audit-only scripts belong here.

## Boundary

- Populace packages must not import from this repository.
- Benchmark jobs must take explicit artifact paths; they must not discover
  candidates or baselines from local working directories.
- US incumbent comparisons must use the certified pinned production baseline
  recorded in `benchmarks/us/incumbent-comparison/manifests/`.
- Local or development baselines are useful for debugging only and are not
  promotion-valid.

## Current Benchmark Areas

| Area | Path | Purpose |
| --- | --- | --- |
| US incumbent comparison | `benchmarks/us/incumbent-comparison/` | Compare candidate Populace-US artifacts with the certified production incumbent on the frozen target surface. |
| Historical archives | `archive/` | Small scorecards and run notes that document past candidate decisions. Large HDF5 artifacts stay in object storage or the local artifact cache. |

## Promotion Rule

A candidate can only replace an incumbent when the benchmark output is
reproducible from explicit inputs, the export/support/lineage gates are green,
and the candidate beats the pinned incumbent on every promotion metric defined
by the benchmark manifest.
