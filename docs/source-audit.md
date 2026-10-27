# Source notes and reproducibility

Reviewed October 27, 2026. This document distinguishes the original presented poster, saved code, and project context supplied by James.

## Available evidence

The public repository contains two course-era Quarto sources. A locally available copy of the private original also contains survey extracts, rendered HTML, cached R objects, and exploratory plots. The inspected HTML does not supply final coefficient/performance tables. James subsequently supplied the original presentation poster, now preserved unchanged at `poster/stat551-poster.pdf`. It is titled *Alcohol Consumption Trends in the United States* and credits Jose Garcia and James Riggs. The poster contains plotted results but no held-out performance table or coefficient/uncertainty table.

Both saved CSV input extracts contain 50,000 data rows, counted with a CSV parser. James's supplied project summary describes approximately 21,500 USCDI records; the exact filtering stage is unverified. Do not use that number as a verified final model sample size.

## Evidence from the original poster

The original poster describes two pipelines: individual-level elastic net and random forest, and state-level elastic net using a top-quartile liver-mortality burden outcome. It includes age-group binge-drinking rates, a mental-health comparison, random-forest feature importance, and a state burden map.

Reported findings include higher binge-drinking rates among adults 18-34, lower rates among adults 55+, associations with poor mental health, income and education, and state-level mortality-burden patterns. Associations with smoking and exercise weakened after age was included. The conclusion reports poorer general health/lower income in higher-burden areas. These are findings reported by the presented artifact, not independently rerun estimates.

The poster itself emphasizes self-report, sampling, cross-sectional limitations, and association rather than causation. Its mortality terminology should be read alongside its liver-mortality target: chronic liver disease is broader than alcohol-attributable mortality.

The faculty-presentation context and approximately 21,500-record USCDI scope were supplied by James; the poster does not state that record count. No additional numeric effect sizes or performance results have been inferred from the plots.

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

The existing public Quarto sources, research documentation, and original poster supplied by James are published. The poster PDF is preserved byte-for-byte; the generated portfolio summary poster is not linked or used. Raw extracts, caches, and private generated HTML remain unpublished. Teammate attribution is retained. Chronic liver disease is not equated with alcohol-attributable death.
