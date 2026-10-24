# Week 3: correlation, causation and confounding

Pooled correlation between year and stunting across all country-years: -0.02.
Within-country correlations: min -0.16, median -0.05, max 0.13.
The pooled number and the within-country numbers are not the same quantity, and the gap
between them is country itself acting as a confounder: countries differ in level and in
trend, and pooling mixes the two.

The causal claim a reader will want to make, stunting fell because of something done
between 2000 and 2024, is not licensed by any correlation here. Every country experienced
the period, so there is no untreated comparison inside the frame.

Directed acyclic graph, in words: interventions and economic growth affect stunting;
country determines both the starting level and the mix of interventions; year is a proxy
for everything that changed over time. Conditioning on country removes the level
confounding but not the time confounding, which is why week 6 needs a design rather
than a correlation.
