# 2026-07-02 — sparse-57k input-mass parity vs dense f0af251

Decision record for the input-mass parity comparison that quantified
populace issue [#278](https://github.com/PolicyEngine/populace/issues/278).

- **Candidate**: `populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701`
  (certified default of policyengine bundle 4.18.8), `populace_us_2024.h5`
  sha256 `c2065b642ab00da74746afdfd9f06890e5f32f9b10bd6610ff236452d40f39c5`.
- **Reference**: `populace-us-2024-f0af251-703bd81a565c-20260620` (certified
  default of bundle 4.18.7), sha256
  `16be6338f9d0b3c339883dae59949e995663b64cf145de6728b3dd0f916c5d5f`, both
  pinned in
  `benchmarks/us/input-mass-parity/manifests/pinned-populace-us-releases-20260702.json`.
- **Heritage context** (diagnostic only): a local us-data enhanced CPS 2024
  build, sha256 recorded in the result JSON — not a certified baseline.
- **Command**: `benchmarks/us/input-mass-parity/run_input_mass_parity.py`
  with default tolerance ±50% and $1B materiality floor; engine
  policyengine-us 1.755.5 (recorded in the JSON).

## Outcome

**FAIL — 72 material engine-input columns lost their mass** (zeroed, absent,
or beyond ±50%), including the four bases issue #278 named
(`traditional_ira_contributions_desired`,
`self_employed_pension_contributions_desired`, `health_savings_account_ald`,
`spm_unit_pre_subsidy_childcare_expenses`) plus `roth_ira_contributions_desired`,
asset stocks (`net_worth`, `stock_assets`, `bank_account_assets`), QBID wage
and property bases, every `takes_up_*` flag, `tip_income`,
`pre_subsidy_rent`, `veterans_benefits`, `workers_compensation`, and the
pre-LSR hours channel. Full table: `input_mass_parity.md`; machine-readable:
`input_mass_parity.json`.

## Decision

**Diagnostic-only** — the sparse-57k release was already certified when this
ran. It drove populace issue #278 and PR
[#279](https://github.com/PolicyEngine/populace/pull/279) (merged
`44868be`), which carries the four named bases through the sparse pipeline
and installs `input_mass_parity_gate` as a release blocker. The next sparse
rebuild must pass this benchmark against the dense f0af251 reference, with
reviewed waivers for any intentionally dropped column.
