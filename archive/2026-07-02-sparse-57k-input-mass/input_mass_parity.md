# US input-mass parity

- engine: policyengine-us 1.755.5
- reference: `populace-us-2024-f0af251-703bd81a565c-20260620` (`16be6338f9d0…`)
- candidate: `populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701` (`c2065b642ab0…`)
- gate: **FAIL** (72 failure(s) at ±50%, floor 1e+09)

## Gate failures

- alimony_expense: populace-us-2024-f0af251-703bd81a565c-20260620 carries 6.46454e+09 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- alimony_income: populace-us-2024-f0af251-703bd81a565c-20260620 carries 2.79892e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- auto_loan_balance: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.30265e+12 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- auto_loan_interest: populace-us-2024-f0af251-703bd81a565c-20260620 carries 6.87146e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- bank_account_assets: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.30585e+13 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- bond_assets: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.22969e+12 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- casualty_loss: populace-us-2024-f0af251-703bd81a565c-20260620 carries 6.7659e+09 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- child_support_expense: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.79495e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- child_support_received: populace-us-2024-f0af251-703bd81a565c-20260620 carries 3.6089e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- detailed_occupation_recode: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.02951e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- disability_benefits: populace-us-2024-f0af251-703bd81a565c-20260620 carries 3.78709e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- domestic_production_ald: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.2326e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- educational_assistance: populace-us-2024-f0af251-703bd81a565c-20260620 carries 8.54459e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- educator_expense: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.47474e+09 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- employer_sponsored_insurance_premiums: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.12952e+12 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- estate_income: populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701 mass 9.84339e+10 vs populace-us-2024-f0af251-703bd81a565c-20260620 5.91586e+10 (+66.4%, beyond ±50%); carry the input through the build or add a reviewed exclusion.
- farm_income: populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701 mass 6.23873e+10 vs populace-us-2024-f0af251-703bd81a565c-20260620 -8.20727e+10 (+176.0%, beyond ±50%); carry the input through the build or add a reviewed exclusion.
- farm_operations_income: populace-us-2024-f0af251-703bd81a565c-20260620 carries -8.20727e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- farm_rent_income: populace-us-2024-f0af251-703bd81a565c-20260620 carries 2.0689e+09 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- financial_assistance: populace-us-2024-f0af251-703bd81a565c-20260620 carries 3.94552e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- first_home_mortgage_balance: populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701 mass 8.19483e+12 vs populace-us-2024-f0af251-703bd81a565c-20260620 2.39907e+13 (-65.8%, beyond ±50%); carry the input through the build or add a reviewed exclusion.
- first_home_mortgage_origination_year: populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701 mass 5.20291e+10 vs populace-us-2024-f0af251-703bd81a565c-20260620 2.15013e+11 (-75.8%, beyond ±50%); carry the input through the build or add a reviewed exclusion.
- fsla_overtime_premium: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.02827e+11 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- health_savings_account_ald: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.04777e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- hourly_wage: populace-us-2024-f0af251-703bd81a565c-20260620 carries 4.46019e+09 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- hours_worked_last_week: populace-us-2024-f0af251-703bd81a565c-20260620 carries 6.05651e+09 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- household_vehicles_value: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.95281e+12 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- investment_income_elected_form_4952: populace-us-2024-f0af251-703bd81a565c-20260620 carries 5.41689e+09 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- investment_interest_expense: populace-us-2024-f0af251-703bd81a565c-20260620 carries 8.89819e+09 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- long_term_capital_gains_on_collectibles: populace-us-2024-f0af251-703bd81a565c-20260620 carries 6.81445e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- miscellaneous_income: populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701 mass 4.74006e+10 vs populace-us-2024-f0af251-703bd81a565c-20260620 1.43872e+10 (+229.5%, beyond ±50%); carry the input through the build or add a reviewed exclusion.
- net_worth: populace-us-2024-f0af251-703bd81a565c-20260620 carries 2.2336e+14 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- non_sch_d_capital_gains: populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701 mass 7.57467e+10 vs populace-us-2024-f0af251-703bd81a565c-20260620 1.14292e+10 (+562.7%, beyond ±50%); carry the input through the build or add a reviewed exclusion.
- other_health_insurance_premiums: populace-us-2024-f0af251-703bd81a565c-20260620 carries 3.41194e+11 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- partnership_income: populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701 mass 8.47756e+11 vs populace-us-2024-f0af251-703bd81a565c-20260620 3.97119e+11 (+113.5%, beyond ±50%); carry the input through the build or add a reviewed exclusion.
- pre_subsidy_rent: populace-us-2024-f0af251-703bd81a565c-20260620 carries 5.89998e+11 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- qualified_reit_and_ptp_income: populace-us-2024-f0af251-703bd81a565c-20260620 carries 5.51968e+09 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- qualified_tuition_expenses: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.61573e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- rental_income: populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701 mass 4.3287e+11 vs populace-us-2024-f0af251-703bd81a565c-20260620 1.9601e+11 (+120.8%, beyond ±50%); carry the input through the build or add a reviewed exclusion.
- roth_401k_contributions_desired: populace-us-2024-f0af251-703bd81a565c-20260620 carries 5.36715e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- roth_ira_contributions_desired: populace-us-2024-f0af251-703bd81a565c-20260620 carries 2.50015e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- salt_refund_income: populace-us-2024-f0af251-703bd81a565c-20260620 carries 4.44016e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- second_home_mortgage_balance: populace-us-2024-f0af251-703bd81a565c-20260620 carries 9.02132e+11 but populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701 mass is zero (-100.0%); carry the input through the build or add a reviewed exclusion.
- second_home_mortgage_interest: populace-us-2024-f0af251-703bd81a565c-20260620 carries 3.94632e+09 but populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701 mass is zero (-100.0%); carry the input through the build or add a reviewed exclusion.
- second_home_mortgage_origination_year: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.71928e+10 but populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701 mass is zero (-100.0%); carry the input through the build or add a reviewed exclusion.
- self_employed_pension_contributions_desired: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.00761e+09 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- self_employment_income_last_year: populace-us-2024-f0af251-703bd81a565c-20260620 carries 2.22674e+11 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- short_term_capital_gains: populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701 mass 1.18072e+11 vs populace-us-2024-f0af251-703bd81a565c-20260620 -7.38298e+09 (+1699.3%, beyond ±50%); carry the input through the build or add a reviewed exclusion.
- social_security_survivors: populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701 mass 1.60985e+11 vs populace-us-2024-f0af251-703bd81a565c-20260620 1.06603e+11 (+51.0%, beyond ±50%); carry the input through the build or add a reviewed exclusion.
- spm_unit_energy_subsidy: populace-us-2024-f0af251-703bd81a565c-20260620 carries 4.04878e+09 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- spm_unit_pre_subsidy_childcare_expenses: populace-us-2024-f0af251-703bd81a565c-20260620 carries 7.47115e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- sstb_self_employment_income_before_lsr: populace-us-2024-f0af251-703bd81a565c-20260620 carries 2.06332e+11 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- sstb_unadjusted_basis_qualified_property: populace-us-2024-f0af251-703bd81a565c-20260620 carries 2.46039e+11 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- sstb_w2_wages_from_qualified_business: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.9147e+11 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- stock_assets: populace-us-2024-f0af251-703bd81a565c-20260620 carries 2.97142e+13 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- survivor_benefits: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.11661e+11 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- tax_exempt_ira_distributions: populace-us-2024-f0af251-703bd81a565c-20260620 carries 2.73593e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- tax_exempt_private_pension_income: populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701 mass 2.23258e+11 vs populace-us-2024-f0af251-703bd81a565c-20260620 8.37715e+11 (-73.3%, beyond ±50%); carry the input through the build or add a reviewed exclusion.
- taxable_401k_distributions: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.24321e+11 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- taxable_403b_distributions: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.60164e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- taxable_sep_distributions: populace-us-2024-f0af251-703bd81a565c-20260620 carries 6.33801e+09 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- tip_income: populace-us-2024-f0af251-703bd81a565c-20260620 carries 5.90758e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- traditional_401k_contributions_desired: populace-us-2024-f0af251-703bd81a565c-20260620 carries 3.04138e+11 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- traditional_ira_contributions_desired: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.61194e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- treasury_tipped_occupation_code: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.04895e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- unadjusted_basis_qualified_property: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.89103e+12 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- unrecaptured_section_1250_gain: populace-us-2024-f0af251-703bd81a565c-20260620 carries 6.08515e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- unreimbursed_business_employee_expenses: populace-us-2024-f0af251-703bd81a565c-20260620 carries 2.18287e+11 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- veterans_benefits: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.77433e+11 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- w2_wages_from_qualified_business: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.40376e+11 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- weekly_hours_worked_before_lsr: populace-us-2024-f0af251-703bd81a565c-20260620 carries 1.35144e+10 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.
- workers_compensation: populace-us-2024-f0af251-703bd81a565c-20260620 carries 7.81908e+09 but the column is absent from populace-us-2024-sparse-l0-refit-57k-71a0887-national-only-20260701; carry the input through the build or add a reviewed exclusion.

## Weighted totals (engine-input variables)

| variable | enhanced-cps-2024-local-build | reference | candidate |
|---|---:|---:|---:|
| `age` | 13.3B | 13.4B | 13.5B |
| `alimony_expense` | 12.6B | 6.5B | — |
| `alimony_income` | 12.8B | 28.0B | — |
| `amt_foreign_tax_credit` | 43.1B | — | — |
| `attends_eligible_educational_institution_for_american_opportunity_credit` | — | 5.7M | — |
| `auto_loan_balance` | 1,240.7B | 1,302.6B | — |
| `auto_loan_interest` | 80.0B | 68.7B | — |
| `bank_account_assets` | 4,657.3B | 13,058.5B | — |
| `bond_assets` | 925.0B | 1,229.7B | — |
| `business_is_sstb` | 9.0M | 5.2M | — |
| `casualty_loss` | 0.8M | 6.8B | — |
| `charitable_cash_donations` | 190.6B | 300.8B | 230.6B |
| `charitable_non_cash_donations` | 152.6B | 70.2B | 52.8B |
| `child_support_expense` | 32.5B | 17.9B | — |
| `child_support_received` | 33.1B | 36.1B | — |
| `congressional_district_geoid` | — | 438.9B | 367.9B |
| `county_fips` | 4.1B | — | — |
| `cps_race` | 534.5M | 527.6M | — |
| `detailed_occupation_recode` | 10.5B | 10.3B | — |
| `disability_benefits` | 42.8B | 37.9B | — |
| `domestic_production_ald` | 35.8B | 12.3B | — |
| `early_withdrawal_penalty` | 4.5B | — | — |
| `educational_assistance` | — | 85.4B | — |
| `educator_expense` | 517.6M | 1.5B | — |
| `employer_sponsored_insurance_premiums` | — | 1,129.5B | — |
| `employment_income_before_lsr` | 10,357.0B | 9,709.0B | 9,711.1B |
| `estate_income` | 62.2B | 59.2B | 98.4B |
| `estate_income_would_be_qualified` | 334.8M | 337.9M | — |
| `excess_withheld_payroll_tax` | 4.9B | — | — |
| `farm_income` | 22.5B | -82.1B | 62.4B |
| `farm_operations_income` | -69.5B | -82.1B | — |
| `farm_operations_income_would_be_qualified` | 334.8M | 337.9M | — |
| `farm_rent_income` | 5.9B | 2.1B | — |
| `farm_rent_income_would_be_qualified` | 334.8M | 337.9M | — |
| `financial_assistance` | — | 39.5B | — |
| `first_home_mortgage_balance` | 2,493.3B | 23,990.7B | 8,194.8B |
| `first_home_mortgage_interest` | 691.2B | 244.0B | 310.8B |
| `first_home_mortgage_origination_year` | 28.2B | 215.0B | 52.0B |
| `fsla_overtime_premium` | — | 102.8B | — |
| `general_business_credit` | 14.2B | — | — |
| `has_american_opportunity_credit_1098_t_or_exception` | — | 5.7M | — |
| `has_american_opportunity_credit_institution_ein` | — | 5.7M | — |
| `has_champva_health_coverage_at_interview` | 1.6M | 1.0M | 0.3M |
| `has_esi` | 175.8M | 197.7M | 153.2M |
| `has_indian_health_service_coverage_at_interview` | 1.1M | 0.8M | 0.4M |
| `has_marketplace_health_coverage` | 13.7M | 20.8M | 21.5M |
| `has_marketplace_health_coverage_at_interview` | 13.7M | 20.8M | 21.5M |
| `has_medicaid_health_coverage_at_interview` | 58.2M | 46.9M | 25.0M |
| `has_never_worked` | 94.6M | 97.8M | — |
| `has_non_marketplace_direct_purchase_health_coverage_at_interview` | 20.3M | 14.9M | 8.0M |
| `has_other_means_tested_health_coverage_at_interview` | 0.5M | 0.4M | 0.2M |
| `has_tricare_health_coverage_at_interview` | 6.0M | 6.9M | 4.2M |
| `has_va_health_coverage_at_interview` | 3.6M | 3.3M | 1.0M |
| `health_insurance_premiums_without_medicare_part_b` | 373.8B | 373.7B | 339.6B |
| `health_savings_account_ald` | 2.4B | 10.5B | — |
| `home_mortgage_interest` | 691.2B | 247.9B | 311.1B |
| `hourly_wage` | 4.9B | 4.5B | — |
| `hours_worked_last_week` | 5.7B | 6.1B | — |
| `household_vehicles_owned` | 206.9M | 142.5M | — |
| `household_vehicles_value` | 3,789.8B | 1,952.8B | — |
| `investment_income_elected_form_4952` | 755.0M | 5.4B | — |
| `investment_interest_expense` | 43.7B | 8.9B | — |
| `is_blind` | 6.0M | 10.6M | — |
| `is_computer_scientist` | 4.7M | 6.0M | — |
| `is_disabled` | 39.6M | 42.5M | — |
| `is_enrolled_at_least_half_time_for_american_opportunity_credit` | — | 5.7M | — |
| `is_executive_administrative_professional` | 88.6M | 92.5M | — |
| `is_farmer_fisher` | 1.2M | 0.9M | — |
| `is_female` | 170.8M | 176.8M | 172.7M |
| `is_full_time_college_student` | 16.8M | 12.7M | — |
| `is_hispanic` | 66.1M | 73.9M | — |
| `is_household_head` | 153.8M | 144.3M | — |
| `is_military` | 0.3M | 0.7M | — |
| `is_paid_hourly` | 88.4M | 66.0M | — |
| `is_pregnant` | 3.1M | 3.7M | — |
| `is_pursuing_credential_for_american_opportunity_credit` | — | 5.7M | — |
| `is_related_to_head_or_spouse` | — | 337.5M | 338.9M |
| `is_separated` | 7.3M | 8.2M | — |
| `is_surviving_spouse` | 22.1M | 12.9M | — |
| `is_union_member_or_covered` | 13.9M | 13.1M | — |
| `is_unmarried_partner_of_household_head` | — | 6.9M | — |
| `is_wic_at_nutritional_risk` | 334.8M | 337.9M | — |
| `keogh_distributions` | 0.0M | 1.4M | — |
| `long_term_capital_gains_before_response` | 1,226.4B | 1,091.1B | 864.4B |
| `long_term_capital_gains_on_collectibles` | 5.6B | 68.1B | — |
| `miscellaneous_income` | 105.5B | 14.4B | 47.4B |
| `net_worth` | 165,809.2B | 223,359.6B | — |
| `non_qualified_dividend_income` | 147.7B | 102.2B | 101.3B |
| `non_sch_d_capital_gains` | 13.2B | 11.4B | 75.7B |
| `other_credits` | 154.4M | — | — |
| `other_health_insurance_premiums` | 312.3B | 341.2B | — |
| `other_medical_expenses` | 274.2B | 287.4B | 283.5B |
| `over_the_counter_health_expenses` | 70.6B | 68.7B | 63.8B |
| `own_children_in_household` | 155.8M | 175.4M | — |
| `partnership_income` | — | 397.1B | 847.8B |
| `partnership_s_corp_income_would_be_qualified` | 334.8M | 337.9M | — |
| `partnership_self_employment_net_earnings` | — | — | 61.7B |
| `pre_subsidy_rent` | 787.0B | 590.0B | — |
| `previous_year_income_available` | 74.1M | 113.7M | — |
| `prior_year_minimum_tax_credit` | 20.1B | — | — |
| `qualified_bdc_income` | 1.9B | 146.3M | — |
| `qualified_dividend_income` | 351.7B | 309.4B | 296.2B |
| `qualified_reit_and_ptp_income` | 20.3B | 5.5B | — |
| `qualified_tuition_expenses` | 868.1M | 16.2B | — |
| `real_estate_taxes` | 486.6B | 261.2B | 201.1B |
| `recapture_of_investment_credit` | 0.3M | — | — |
| `receives_housing_assistance` | — | 6.0M | — |
| `receives_wic` | 0.0M | 2.9M | — |
| `rental_income` | 301.6B | 196.0B | 432.9B |
| `rental_income_would_be_qualified` | 334.8M | 337.9M | — |
| `roth_401k_contributions_desired` | — | 53.7B | — |
| `roth_ira_contributions_desired` | — | 25.0B | — |
| `s_corp_income` | — | 0.0M | 0.0M |
| `salt_refund_income` | 48.1B | 44.4B | — |
| `second_home_mortgage_balance` | 0.0M | 902.1B | 0.0M |
| `second_home_mortgage_interest` | 0.0M | 3.9B | 0.0M |
| `second_home_mortgage_origination_year` | 0.0M | 17.2B | 0.0M |
| `selected_marketplace_plan_benchmark_ratio` | 186.9M | 174.4M | 158.5M |
| `self_employed_pension_contributions_desired` | — | 1.0B | — |
| `self_employment_income_before_lsr` | 280.8B | 389.2B | 419.6B |
| `self_employment_income_last_year` | 126.4B | 222.7B | — |
| `self_employment_income_would_be_qualified` | 287.0M | 337.9M | — |
| `short_term_capital_gains` | -184.7B | -7.4B | 118.1B |
| `social_security_dependents` | 94.9B | 49.7B | 51.1B |
| `social_security_disability` | 218.0B | 145.8B | 147.1B |
| `social_security_retirement` | — | 1,104.8B | 1,111.7B |
| `social_security_survivors` | 211.5B | 106.6B | 161.0B |
| `spm_unit_energy_subsidy` | — | 4.0B | — |
| `spm_unit_net_income_reported` | 10,942.1B | — | — |
| `spm_unit_pre_subsidy_childcare_expenses` | 182.5B | 74.7B | — |
| `spm_unit_total_income_reported` | 14,780.4B | — | — |
| `ssi_reported` | 45.1B | — | — |
| `sstb_self_employment_income_before_lsr` | 1.8B | 206.3B | — |
| `sstb_self_employment_income_would_be_qualified` | — | 5.2M | — |
| `sstb_unadjusted_basis_qualified_property` | 11.9B | 246.0B | — |
| `sstb_w2_wages_from_qualified_business` | 183.5B | 191.5B | — |
| `state_fips` | 4.2B | 4.4B | 3.7B |
| `stock_assets` | 6,897.1B | 29,714.2B | — |
| `strike_benefits` | 0.0M | — | — |
| `student_loan_interest` | 5.8B | 19.4B | 10.4B |
| `survivor_benefits` | — | 111.7B | — |
| `takes_up_aca_if_eligible` | 129.2M | 8.4M | 7.8M |
| `takes_up_dc_ptc` | 58.5M | 176.5M | — |
| `takes_up_early_head_start_if_eligible` | 26.7M | 337.9M | — |
| `takes_up_eitc` | 136.3M | 176.5M | — |
| `takes_up_head_start_if_eligible` | 101.9M | 337.9M | — |
| `takes_up_housing_assistance_if_eligible` | — | 48.0M | — |
| `takes_up_medicaid_if_eligible` | 276.2M | 337.9M | — |
| `takes_up_medicare_if_eligible` | — | 337.9M | — |
| `takes_up_snap_if_eligible` | 132.3M | 158.8M | — |
| `takes_up_ssi_if_eligible` | 165.8M | 337.9M | — |
| `takes_up_tanf_if_eligible` | 36.8M | 158.8M | — |
| `tax_exempt_401k_distributions` | 0.0M | — | — |
| `tax_exempt_403b_distributions` | 0.0M | — | — |
| `tax_exempt_interest_income` | 82.6B | 55.6B | 54.1B |
| `tax_exempt_ira_distributions` | 5.1B | 27.4B | — |
| `tax_exempt_private_pension_income` | 682.0B | 837.7B | 223.3B |
| `tax_exempt_sep_distributions` | 0.0M | — | — |
| `taxable_401k_distributions` | 37.4B | 124.3B | — |
| `taxable_403b_distributions` | 7.8B | 16.0B | — |
| `taxable_interest_income` | 299.8B | 522.6B | 320.2B |
| `taxable_ira_distributions` | 441.2B | 432.8B | 430.1B |
| `taxable_private_pension_income` | 920.1B | 893.3B | 889.1B |
| `taxable_sep_distributions` | 1.2B | 6.3B | — |
| `tip_income` | 51.6B | 59.1B | — |
| `traditional_401k_contributions_desired` | — | 304.1B | — |
| `traditional_ira_contributions_desired` | — | 16.1B | — |
| `treasury_tipped_occupation_code` | 11.9B | 10.5B | — |
| `unadjusted_basis_qualified_property` | 2,052.2B | 1,891.0B | — |
| `unemployment_compensation` | 35.2B | 28.3B | 29.7B |
| `unrecaptured_section_1250_gain` | 45.7B | 60.9B | — |
| `unreimbursed_business_employee_expenses` | 123.3B | 218.3B | — |
| `unreported_payroll_tax` | 0.0M | — | — |
| `veterans_benefits` | 130.9B | 177.4B | — |
| `w2_wages_from_qualified_business` | 847.2B | 140.4B | — |
| `weekly_hours_worked_before_lsr` | 6.5B | 13.5B | — |
| `weeks_unemployed` | 187.2M | 210.5M | — |
| `workers_compensation` | 9.9B | 7.8B | — |
| `would_claim_wic` | 334.8M | 337.9M | — |
| `would_file_taxes_voluntarily` | 3.3M | 6.8M | — |
