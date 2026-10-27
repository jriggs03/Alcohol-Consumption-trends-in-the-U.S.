# Source notes and reproducibility

Reviewed October 27, 2026. This document distinguishes available source evidence from the project summary supplied by James.

## Available evidence

The public repository contains two course-era Quarto sources. A locally available copy of the private original also contains survey extracts, rendered HTML, cached R objects, and exploratory plots. The inspected HTML does not supply final coefficient/performance tables. No original faculty slide deck or final report was located in the inspected project folders or Downloads inventory.

Both saved CSV input extracts contain 50,000 data rows, counted with a CSV parser. James's supplied project summary describes approximately 21,500 USCDI records; the exact filtering stage is unverified. Do not use that number as a verified final model sample size.

## What comes from the supplied project summary

- Presentation to Cal Poly Statistics faculty.
- Younger adults had higher odds of binge drinking.
- State-level associations between poorer general health/lower income and alcohol-related deaths.

These qualitative findings are reported as project findings. Effect sizes, uncertainty, and model performance cannot be reconstructed from the available summary alone. The poster intentionally contains no invented empirical charts or numeric performance results.

## What the code supports

- BRFSS classification, R/tidymodels, regularized logistic regression via glmnet.
- A random-forest specification using ranger in `Jose.qmd`.
- Five-fold cross-validation and ROC AUC tuning specifications.
- Aggregating BRFSS measures and joining to USCDI by state in James's source.
- Different USCDI target constructions across the two analyses: broad alcohol/liver indicators versus chronic liver disease mortality.

## Issues to resolve before reproduction

1. James's source uses broad missing-value recoding across all fields; legitimate codes can be discarded. Confirm each variable against its year-specific codebook and report post-cleaning counts.
2. In `Jose.qmd`, `educ` is referenced after the input column is named `edu`. The random-forest workflow refers to an undefined `rf_recipe`. Resolve these names and review outcome labels against the source codebook.
3. One teammate USCDI workflow derives `HighBurden` from `Mortality` and leaves `Mortality` among the predictors. This leaks the target definition. Remove the defining variable before evaluation; do not report current metrics as predictive evidence.
4. James's broad state-level target mixes indicator definitions, units, years, and strata. Define a comparable outcome, use suitable state/year grouping during validation, and address repeated state observations before interpreting results.
5. Review survey weights, missingness, selection, class balance, and held-out evaluation. Cross-validation tuning alone is not a verified held-out result. Avoid selecting the largest metric across different metric scales.
6. Review the interpretation of numeric averages of categorical income/health codes and distinguish aggregate associations from individual effects.
7. Restore data paths and dependencies and preserve an environment specification. The saved course sources are not a turnkey reproducible pipeline.

## Publication scope

Only the existing public Quarto sources, research documentation, and a newly prepared summary poster are used. Raw extracts, caches, and private generated HTML remain unpublished. Teammate attribution is retained. Chronic liver disease is not equated with alcohol-attributable death.
