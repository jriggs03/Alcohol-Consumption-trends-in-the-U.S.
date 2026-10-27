# Alcohol Consumption Trends in the United States

Applied Statistical Research Project · STAT 551 · Cal Poly Statistics

**Jose Garcia and James Riggs**

## Problem

Explore demographic, socioeconomic, and health associations with binge drinking; separately examine state-level alcohol-related health outcomes.

## Data

BRFSS: 50,000 input survey rows before cleaning. USCDI: state-level indicators, with an approximately 21,500-record analysis scope reported in the supplied project summary. The saved USCDI input extract has 50,000 rows; the filtering stage for the reported scope is unverified. The poster does not establish these sample sizes.

## Methods

The original poster describes elastic net and random forest for individual-level binge-drinking analysis, and elastic net for state-level mortality burden. High burden is defined as the top 25% of states by liver mortality. The Quarto sources use R/tidymodels, glmnet, ranger, five-fold cross-validation, and ROC AUC tuning specifications.

## Findings from the original poster

- Adults aged 18-34 had the highest binge-drinking rates; those 55+ had lower rates.
- More poor-mental-health days were associated with a higher likelihood of binge drinking.
- Lower education and income were associated with slightly higher individual-level risk.
- Higher state binge-drinking rates and lower income/education were associated with greater mortality burden; the conclusion also notes poorer general health in higher-burden areas.
- Associations with smoking and exercise weakened after age was included.

The poster contains age-group, mental-health, random-forest importance, and state-burden plots. No unreported numeric effects or held-out performance claims have been added. These are presented findings, not a new reproduction.

## Presentation and takeaways

James Riggs presented this team project to Cal Poly Statistics faculty. The original poster credits Jose Garcia and James Riggs. It connects data preparation, statistical learning, and communicating observational findings and limitations.

## Artifacts and limitations

[Original research poster (PDF)](../poster/stat551-poster.pdf) · [Website case study](https://jriggs03.github.io/stat551.html) · [Source audit](source-audit.md)

The supplied poster is published unchanged. State-level results do not establish individual risk or causation; chronic liver disease mortality is broader than alcohol-attributable mortality. Self-report, phone-based sampling, and cross-sectional design limit interpretation. The saved Quarto sources need the reproducibility review documented in the source audit.
