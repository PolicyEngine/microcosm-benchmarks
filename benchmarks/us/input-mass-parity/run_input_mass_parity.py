"""Input-mass parity benchmark: does a release keep its input surface alive?

A calibrated release can hit its entire target surface while carrying ~$0 in
input bases the prior certified release populates — every reform touching
those bases then silently scores ~$0 (populace issue #278: the sparse-57k
default zeroed IRA/HSA/pension-contribution/childcare inputs). This runner
compares weighted per-column totals of persisted engine-input variables
between explicit artifacts and applies
:func:`populace.build.gates.input_mass_parity_gate`.

Inputs are explicit paths (repo rule: no local-directory discovery); every
input's sha256 is embedded in the output so archived results are auditable.

Example:
    uv run benchmarks/us/input-mass-parity/run_input_mass_parity.py \
        --reference-h5 /path/to/dense/populace_us_2024.h5 \
        --reference-name populace-us-2024-f0af251 \
        --candidate-h5 /path/to/sparse/populace_us_2024.h5 \
        --candidate-name populace-us-2024-sparse-l0-refit-57k \
        --flat-incumbent-h5 /path/to/enhanced_cps_2024.h5 \
        --flat-incumbent-name enhanced-cps-2024-local \
        --out results/
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import h5py
import numpy as np
import pandas as pd

from populace.build.gates import input_mass_parity_gate
from populace.build.us_runtime.input_mass import us_input_mass_totals
from populace.build.us_runtime.l0_refit_export import load_us_frame
from populace.frame.adapters.policyengine_us import PolicyEngineUSEngine

STRUCTURAL = frozenset(
    {
        "person_id",
        "household_id",
        "tax_unit_id",
        "spm_unit_id",
        "family_id",
        "marital_unit_id",
        "person_household_id",
        "person_tax_unit_id",
        "person_spm_unit_id",
        "person_family_id",
        "person_marital_unit_id",
        "household_weight",
        "person_weight",
        "tax_unit_weight",
        "spm_unit_weight",
        "family_weight",
        "marital_unit_weight",
    }
)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def flat_us_data_totals(path: Path) -> dict[str, float]:
    """Weighted totals for a flat us-data H5 (variable groups keyed by period).

    Entity weights follow the PolicyEngine convention: each entity inherits
    its containing household's weight through membership; group-entity weight
    is the first member's household weight.
    """

    with h5py.File(path, "r") as f:

        def arr(name: str) -> np.ndarray:
            group = f[name]
            period = sorted(group.keys())[0]
            return np.asarray(group[period][...])

        household_weight = arr("household_weight").astype(np.float64)
        household_index = pd.Series(
            np.arange(len(arr("household_id"))), index=arr("household_id")
        )
        person_weight = household_weight[
            household_index.reindex(arr("person_household_id")).to_numpy()
        ]
        weights_by_length: dict[int, np.ndarray] = {
            len(household_weight): household_weight,
            len(person_weight): person_weight,
        }
        for entity in ("tax_unit", "spm_unit", "family", "marital_unit"):
            ids = arr(f"{entity}_id")
            member = arr(f"person_{entity}_id")
            first = pd.Series(person_weight, index=member).groupby(level=0).first()
            weights_by_length.setdefault(
                len(ids), first.reindex(ids).fillna(0.0).to_numpy()
            )

        totals: dict[str, float] = {}
        for name in f.keys():
            if name in STRUCTURAL or not isinstance(f[name], h5py.Group):
                continue
            values = arr(name)
            if values.dtype.kind in ("S", "U", "O"):
                continue
            weights = weights_by_length.get(len(values))
            if weights is None:
                continue
            numeric = np.nan_to_num(values.astype(np.float64))
            totals[name] = float(numeric @ weights)
        return totals


def _gate_payload(gate) -> dict[str, object]:
    return {
        "passed": gate.passed,
        "failures": list(gate.failures),
        "details": dict(gate.details),
    }


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference-h5", required=True, type=Path)
    parser.add_argument("--reference-name", required=True)
    parser.add_argument("--candidate-h5", required=True, type=Path)
    parser.add_argument("--candidate-name", required=True)
    parser.add_argument(
        "--flat-incumbent-h5",
        type=Path,
        help="Optional flat us-data H5 for heritage context (diagnostic).",
    )
    parser.add_argument("--flat-incumbent-name", default="flat-incumbent")
    parser.add_argument("--relative-tolerance", type=float, default=0.5)
    parser.add_argument("--minimum-reference-total", type=float, default=1e9)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args(argv)

    import importlib.metadata

    engine_version = importlib.metadata.version("policyengine-us")
    input_variables = tuple(PolicyEngineUSEngine().variables())

    reference_totals = us_input_mass_totals(
        load_us_frame(args.reference_h5), columns=input_variables
    )
    candidate_totals = us_input_mass_totals(
        load_us_frame(args.candidate_h5), columns=input_variables
    )
    gate = input_mass_parity_gate(
        candidate_totals,
        reference_totals,
        candidate_name=args.candidate_name,
        reference_name=args.reference_name,
        relative_tolerance=args.relative_tolerance,
        minimum_reference_total=args.minimum_reference_total,
    )

    artifacts = {
        "reference": {
            "name": args.reference_name,
            "path": str(args.reference_h5),
            "sha256": _sha256(args.reference_h5),
        },
        "candidate": {
            "name": args.candidate_name,
            "path": str(args.candidate_h5),
            "sha256": _sha256(args.candidate_h5),
        },
    }
    flat_totals: dict[str, float] | None = None
    if args.flat_incumbent_h5 is not None:
        flat_totals = {
            name: total
            for name, total in flat_us_data_totals(args.flat_incumbent_h5).items()
            if name in set(input_variables)
        }
        artifacts["flat_incumbent"] = {
            "name": args.flat_incumbent_name,
            "path": str(args.flat_incumbent_h5),
            "sha256": _sha256(args.flat_incumbent_h5),
        }

    columns = sorted(
        set(reference_totals) | set(candidate_totals) | set(flat_totals or ())
    )
    rows = [
        {
            "variable": name,
            "reference_total": reference_totals.get(name),
            "candidate_total": candidate_totals.get(name),
            **(
                {"flat_incumbent_total": flat_totals.get(name)}
                if flat_totals is not None
                else {}
            ),
        }
        for name in columns
    ]

    result = {
        "schema_version": 1,
        "kind": "us_input_mass_parity",
        "engine": {"policyengine_us": engine_version},
        "relative_tolerance": args.relative_tolerance,
        "minimum_reference_total": args.minimum_reference_total,
        "artifacts": artifacts,
        "gate": _gate_payload(gate),
        "totals": rows,
    }
    args.out.mkdir(parents=True, exist_ok=True)
    json_path = args.out / "input_mass_parity.json"
    json_path.write_text(json.dumps(result, indent=1, allow_nan=False) + "\n")

    def fmt(x: float | None) -> str:
        if x is None:
            return "—"
        if abs(x) >= 1e9:
            return f"{x / 1e9:,.1f}B"
        return f"{x / 1e6:,.1f}M"

    lines = [
        "# US input-mass parity",
        "",
        f"- engine: policyengine-us {engine_version}",
        f"- reference: `{args.reference_name}` (`{artifacts['reference']['sha256'][:12]}…`)",
        f"- candidate: `{args.candidate_name}` (`{artifacts['candidate']['sha256'][:12]}…`)",
        f"- gate: **{'PASS' if gate.passed else 'FAIL'}** "
        f"({len(gate.failures)} failure(s) at ±{args.relative_tolerance:.0%}, "
        f"floor {args.minimum_reference_total:.0e})",
        "",
    ]
    if gate.failures:
        lines += ["## Gate failures", ""]
        lines += [f"- {failure}" for failure in gate.failures]
        lines += [""]
    header = "| variable | reference | candidate |"
    divider = "|---|---:|---:|"
    if flat_totals is not None:
        header = f"| variable | {args.flat_incumbent_name} | reference | candidate |"
        divider = "|---|---:|---:|---:|"
    lines += ["## Weighted totals (engine-input variables)", "", header, divider]
    for row in rows:
        cells = [f"`{row['variable']}`"]
        if flat_totals is not None:
            cells.append(fmt(row.get("flat_incumbent_total")))
        cells += [fmt(row["reference_total"]), fmt(row["candidate_total"])]
        lines.append("| " + " | ".join(cells) + " |")
    (args.out / "input_mass_parity.md").write_text("\n".join(lines) + "\n")
    print(
        json.dumps(
            {
                "passed": gate.passed,
                "failures": len(gate.failures),
                "columns": len(rows),
                "out": str(json_path),
            }
        )
    )


if __name__ == "__main__":
    main()
