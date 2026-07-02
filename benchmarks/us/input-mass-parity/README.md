# US input-mass parity

Does a candidate release keep its persisted input surface alive? A calibrated
release can hit its entire target surface while carrying ~$0 in input bases
the prior certified release populates — every reform touching those bases
then silently scores ~$0. That is populace issue
[#278](https://github.com/PolicyEngine/populace/issues/278): the certified
sparse-57k default zeroed the IRA-contribution, HSA, pension-contribution,
and childcare inputs, so CDCC repeal scored $0.00B and above-the-line
deduction repeal collapsed from $131B to $41B.

This benchmark compares weighted per-column totals of persisted engine-input
variables between explicit artifacts and applies
`populace.build.gates.input_mass_parity_gate` — the same gate the populace
release builder runs (`--input-mass-reference-h5`, populace PR
[#279](https://github.com/PolicyEngine/populace/pull/279)). Running it here
keeps an auditable archived record per release pair, independent of the
release pipeline.

## Required inputs

- Reference Populace-US HDF5 artifact (the prior certified release, pinned in
  `manifests/`).
- Candidate Populace-US HDF5 artifact.
- Optionally, a flat us-data H5 for heritage context (diagnostic only; record
  its sha256 — local development copies are not certified baselines).
- Explicit output directory.

## Run

```bash
uv run benchmarks/us/input-mass-parity/run_input_mass_parity.py \
    --reference-h5 <dense populace_us_2024.h5> \
    --reference-name populace-us-2024-f0af251 \
    --candidate-h5 <candidate populace_us_2024.h5> \
    --candidate-name <candidate release id> \
    --out <results dir>
```

## Rule

A candidate that loses material persisted input mass against the pinned
prior certified release is not promotion-valid unless every lost column
carries a reviewed waiver naming why the loss is intentional. Zeroed or
absent material columns fail at any drift tolerance.

## Baseline rules

Use only artifacts pinned in `manifests/` for promotion comparisons. The
gate's tolerance (default ±50%) and materiality floor (default $1B weighted)
are recorded in every output.
