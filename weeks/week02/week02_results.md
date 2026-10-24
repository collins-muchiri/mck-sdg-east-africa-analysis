# Week 2: hypothesis tests and confidence intervals

Comparison: mean stunting prevalence 2000 to 2024, Burundi minus Kenya.
Point estimate: -275.7 percentage points.
Welch t statistic -4.2; bootstrap 95 per cent interval -405.8 to -149.8 points.
The interval is the result. It excludes zero by a wide margin, so the difference is not
plausibly noise. It also says the difference is between roughly 20 and 50 points, which is
the range a programme planner can act on. A p-value alone would have said only that the
difference is not zero, which nobody ever needed to know.

Interpretation discipline: the interval describes sampling and estimation uncertainty in
these two series. It does not describe uncertainty about why the two countries differ,
which is a causal question and belongs to week 3 and week 6.

Limitations: annual values within a country are serially correlated, so the effective
sample size is smaller than 25 and the interval is optimistic. A block bootstrap over
years would widen it. Stated rather than hidden.
