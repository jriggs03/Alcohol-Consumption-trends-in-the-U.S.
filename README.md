# Alcohol & Health Outcomes

**Applied Statistical Research Project · STAT 551 · Cal Poly Statistics**

My teammate **Jose Garcia** and I built this statistical learning project for STAT 551 at Cal Poly. We explored demographic and health patterns associated with binge drinking, alongside state-level alcohol-related health indicators. I presented our work to Cal Poly Statistics faculty.

[Read the case study](https://jriggs03.github.io/stat551.html) · [Original research poster (PDF)](poster/stat551-poster.pdf)

## Problem and data

- **Individual level:** classify binge-drinking responses using BRFSS health, demographic, and socioeconomic variables. The saved input extract contains 50,000 rows before cleaning.
- **State level:** explore USCDI alcohol/liver indicators alongside aggregated BRFSS measures. My project summary describes approximately 21,500 indicator records, while the saved input extract contains 50,000 rows. I have not verified which filtering stage corresponds to 21,500, so I do not present either count as a final model sample size.

The two analyses have different units of observation; state-level associations are not individual-level estimates.

## Methods / stack

R, tidyverse, tidymodels, glmnet, ranger, Quarto. We used regularized logistic regression and random forests, with five-fold cross-validation and ROC AUC tuning in the saved sources. My state-level workflow joins aggregated BRFSS measures to USCDI by state.

## Findings reported in the original poster

- Adults aged 18-34 had the highest binge-drinking rates; adults 55+ had lower rates.
- More days of poor mental health were associated with a higher likelihood of binge drinking; lower education and income were associated with slightly higher risk.
- Higher state binge-drinking rates and lower state income/education were associated with greater mortality burden. The conclusion also reports poorer general health in higher-burden areas.
- Associations with smoking and exercise weakened after age was included.

The original poster contains age-group, mental-health, random-forest importance, and state-burden plots. I summarize the findings we presented here; I have not rerun the models for this writeup. I have not added coefficients, uncertainty intervals, or held-out metrics that were not reported.

The poster describes elastic net and random forest at the individual level, and elastic net for a state-level high-burden outcome defined by the top 25% of liver mortality. Chronic liver disease mortality is broader than alcohol-attributable mortality. These observational analyses do not establish causation.

## Files and attribution

- `Classification_project(James).qmd`: my original course analysis.
- `Jose.qmd`: Jose Garcia’s analysis, retained with attribution; this is team work.
- `poster/stat551-poster.pdf`: the original poster we presented, preserved unchanged.
- `docs/source-audit.md`: provenance, known code issues, and reproduction requirements.
- `docs/case-study.md`: research summary and presentation context.

## Reproduction status

I have preserved the original sources as submitted. They need corrections before an end-to-end rerun. Obtain BRFSS/USCDI data independently, install the R libraries declared in each source, update local data paths, and review the issues in [source notes](docs/source-audit.md) before rendering with Quarto. I have left raw survey extracts, generated course HTML, and caches out of this repository.

I keep the original repository private and use this public version for my portfolio.
