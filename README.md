# Alcohol & Health Outcomes

**Applied Statistical Research Project · STAT 551 · Cal Poly Statistics**

A team statistical learning project exploring demographic and health patterns associated with binge drinking, alongside state-level alcohol-related health indicators. James Riggs presented the work to Cal Poly Statistics faculty.

[Read the case study](https://jriggs03.github.io/stat551.html) · [Research poster (PDF)](https://jriggs03.github.io/assets/stat551-poster.pdf)

## Problem and data

- **Individual level:** classify binge-drinking responses using BRFSS health, demographic, and socioeconomic variables. The saved input extract contains 50,000 rows before cleaning.
- **State level:** explore USCDI alcohol/liver indicators alongside aggregated BRFSS measures. The project summary describes approximately 21,500 indicator records; the saved input extract contains 50,000 rows. The exact stage corresponding to 21,500 is not preserved, so neither count is presented as a final model sample size.

The two analyses have different units of observation; state-level associations are not individual-level estimates.

## Methods / stack

R, tidyverse, tidymodels, glmnet, ranger, Quarto. Sources include regularized logistic regression, a teammate random-forest specification, five-fold cross-validation, and ROC AUC tuning. James's state-level workflow joins aggregated BRFSS measures to USCDI by state.

## Reported findings

The project summary reports higher odds of binge drinking among younger adults, and state-level associations between poorer general health/lower income and alcohol-related deaths. These are qualitative reported findings, not independently reproduced results. No verified coefficient tables, uncertainty intervals, or held-out model metrics are available here.

Chronic liver disease mortality in one source is broader than alcohol-attributable mortality. These observational analyses do not establish causation.

## Files and attribution

- `Classification_project(James).qmd`: James Riggs's original course-era analysis.
- `Jose.qmd`: teammate analysis, retained with attribution; this is team work.
- `docs/source-audit.md`: provenance, known code issues, and reproduction requirements.
- `docs/case-study.md`: research summary and presentation context.
- `poster/`: newly prepared portfolio poster and editable generator.

## Reproduction status

The original sources are preserved as submitted and need corrections before an end-to-end rerun. Obtain BRFSS/USCDI data independently, install the R libraries declared in each source, update local data paths, and review the issues in [source notes](docs/source-audit.md) before rendering with Quarto. No raw survey extracts, generated course HTML, or caches are published.

The private original repository is retained. This public repository is the curated portfolio version. The new poster summarizes the supplied project context and source workflows; it is not the original faculty presentation.
