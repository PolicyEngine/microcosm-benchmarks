# microcosm-benchmarks

External benchmark harnesses and archived incumbent comparisons for Microcosm.

This repository is intentionally separate from
[`PolicyEngine/microcosm`](https://github.com/PolicyEngine/microcosm). The live
Microcosm repo owns the library code, build contracts, package tests, release
gates, and published population registry. Incumbent replacement comparisons,
historical candidate scorecards, and audit-only scripts belong here.

## Boundary

- Microcosm packages must not import from this repository.
- Benchmark jobs must take explicit artifact paths; they must not discover
  candidates or baselines from local working directories.
- US incumbent comparisons must use the certified pinned production baseline
  recorded in `benchmarks/us/incumbent-comparison/manifests/`.
- Local or development baselines are useful for debugging only and are not
  promotion-valid.

## Current Benchmark Areas

| Area | Path | Purpose |
| --- | --- | --- |
| US incumbent comparison | `benchmarks/us/incumbent-comparison/` | Compare candidate Microcosm-US artifacts with the certified production incumbent on the frozen target surface. |
| Historical archives | `archive/` | Small scorecards and run notes that document past candidate decisions. Large HDF5 artifacts stay in object storage or the local artifact cache. |

## Promotion Rule

A candidate can only replace an incumbent when the benchmark output is
reproducible from explicit inputs, the export/support/lineage gates are green,
and the candidate beats the pinned incumbent on every promotion metric defined
by the benchmark manifest.

## License

Code in this repository is released under the [MIT License](LICENSE). Original text and figures are released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) with attribution to PolicyEngine. Third-party data and materials keep their own terms.
