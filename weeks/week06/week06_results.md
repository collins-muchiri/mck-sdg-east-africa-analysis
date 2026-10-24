# Week 6: difference-in-differences, and why this one is not causal

Design as taught: treatment assigned to Kenya at 2013, comparison is the mean of the other
seven countries, windows 2008 to 2012 and 2013 to 2024.
Difference-in-differences estimate: -186.7 percentage points.

Why this estimate must not be read causally, in order of severity:
1. Assignment is not a policy. Devolution changed many things at once and only in Kenya,
   so the estimand is the effect of everything that changed in Kenya in 2013, not of any
   intervention.
2. Parallel trends fail visibly before 2013: the treated and comparison series do not move
   together in the pre-window, which is the assumption the estimator lives on.
3. The comparison group is itself treated by regional shocks, so it is not a clean counterfactual.

What the exercise still teaches: how to lay out a DiD, how to plot the pre-trend that
decides whether the design is credible, and how to write the limitation before the
estimate is quoted. A DiD with a failed pre-trend, disclosed, is worth more than a DiD
with a hidden one.

The version worth running professionally: a real programme rollout with staggered
adoption across counties, an event-study plot, and a placebo test on a pre-period.
