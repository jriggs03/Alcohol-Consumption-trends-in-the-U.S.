# Statistical Learning Research: Alcohol & Health Outcomes

## Problem

Explore associations between demographic, socioeconomic, and health characteristics and binge drinking; separately examine state-level alcohol-related health outcomes.

## Data

BRFSS: 50,000 input survey rows before cleaning. USCDI: state-level indicators, with an approximately 21,500-record analysis scope reported in the project summary. The saved USCDI input extract has 50,000 rows; the filtering stage for the reported scope is unverified.

## Methods

R/tidymodels workflows; regularized logistic regression with glmnet, random-forest work with ranger, five-fold cross-validation, and ROC AUC tuning. Aggregate BRFSS measures were joined to USCDI by state in James's workflow.

## Results

Reported qualitative findings: younger adults had higher odds of binge drinking; poorer general health/lower income were associated with alcohol-related deaths at the state level. Final numerical estimates and performance tables are unavailable. See the source audit for code and interpretation limitations.

## Presentation and takeaways

James Riggs presented the team project to Cal Poly Statistics faculty. The work connected data cleaning, model development, and communicating observational findings and limitations. It is course-based research, with teammate work retained as `Jose.qmd`.

## Artifacts

[Website case study](https://jriggs03.github.io/stat551.html) · [Source audit](source-audit.md)

State-level results do not establish individual risk or causation; chronic liver disease mortality is broader than alcohol-attributable mortality.
