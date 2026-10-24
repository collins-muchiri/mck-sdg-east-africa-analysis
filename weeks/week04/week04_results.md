# Week 4: regression with diagnostics

Model: stunting on a linear year term plus country fixed effects, n = 1200.
Year coefficient: -4.223 percentage points per year, the average within-country
annual change once country level differences are absorbed.
Diagnostics: residuals against fitted show a funnel narrowing at high fitted values,
indicating heteroskedasticity, so ordinary standard errors would overstate precision and
cluster-robust errors by country are required before any interval is quoted. Residual
quantiles depart from a straight line in the tails, so the normality convenience used for
intervals is approximate at best.

Reading the coefficient honestly: it is a description of a linear trend within countries
over this period. It is not a policy effect, and extrapolating it beyond 2024 assumes the
trend mechanism continues, which nothing here tests.

What a reviewer should check first: whether the country fixed effects and the year term
are collinear with any omitted time-varying confounder you care about. They are. That is
the week 6 problem.
