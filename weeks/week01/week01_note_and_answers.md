# Week 1 submission: note and check-question answers

Candidate: Muchiri Collins Kamama
Concept: sampling and bias
Data: UN SDG global indicator database, indicator 2.2.1, series SH_STA_STNT, retrieved 24 October 2026
Companion files: week01_sampling_bias.py, week01_raw_sdg_2_2_1.csv, week01_country_coverage.csv, week01_results.md, week01_coverage.png
Status: written for external presentation. The example in answer 3 is drawn from my own programme and is marked for internal verification before any external use.

---

## The note, 508 words

### What a sampling rule costs: three means from one frame

A dataset is not a picture of the world. It is a picture of a process that decided what got written down, and the distance between those two pictures is sampling bias. This note records what I learned pulling SDG 2.2.1, childhood stunting prevalence, for eight East African countries from the UN SDG global indicator database: 1,200 country-year observations, 2000 to 2024, complete coverage for every country.

I asked one question three ways. What is the regional mean stunting prevalence, latest reported year per country, unweighted? Using every country, 30.2 per cent. Using only countries that reported recently, 30.2 per cent, a difference of zero. Using only countries performing better than the regional median, 23.2 per cent, a difference of minus seven points from four of eight countries. No observation changed between the three rows. Only the rule that chose the countries changed. Seven percentage points of regional reality, manufactured by a filter, with every figure technically correct.

The zero is the more instructive result, and I did not expect it. I chose recency as my second rule because in programme data recency selection is everywhere: the partner that reports late is dropped from the average, the county with the thin upload disappears from the trend. I expected it to bite here. It did not, because 2.2.1 is a modelled estimate. The Joint Child Malnutrition Estimates publish a value for every country-year, so the frame contains no missing cells to select on. The gaps were imputed before I arrived. Completeness in that database is a property of the estimation method, not of national statistical systems, and a recency filter has nothing to grip.

That is the first lesson I carry into my own work: missingness can be manufactured away upstream, and a dataset with no holes is not therefore a dataset with no bias. It may simply be a dataset whose holes were filled by someone else's model, with someone else's assumptions, before I ever queried it. The second lesson is the seven points. Selection on the outcome is the bias that survives every data-quality check, because each retained record is perfectly valid. A ministry quoting only its better-performing neighbours is not lying about any number. It is lying about the set.

Both lessons land directly on the monitoring work I do. When I compile a quarterly donor report from implementing-partner submissions, every partner I exclude for lateness is a recency selection, and the late partners are rarely late at random. When a dashboard drops a county for insufficient data, the aggregate that survives is the better-performers sample in a uniform. The defence is not better cleaning. It is disclosure: report what was excluded, why, and which direction the exclusion pushes the number.

Next step in this programme: repeat the exercise on a survey-reported indicator, where countries appear only in survey years, so the recency mechanism becomes visible rather than imputed away.

---

## Check question 1

**Which countries have the fewest reported years in the coverage table, and why is that non-random?**

None of them do, and saying so is the answer. All eight countries report twenty-five consecutive years, 2000 to 2024, with zero missing years in the 2015 to 2024 window. The coverage table therefore cannot show reporting behaviour at all, because indicator 2.2.1 is a modelled estimate: the Joint Child Malnutrition Estimates publish a value for every country-year, so there is no reporting process left to observe.

The question still has a correct general answer, which is where the non-randomness lives. On survey-reported indicators the sparsest coverage in this region belongs to South Sudan and Somalia, and historically to Burundi in crisis years. Survey fielding is postponed by conflict, insecurity, access negotiation and funding gaps. Those same conditions drive the outcomes being measured. The countries least able to produce data are therefore the countries whose populations are most at risk, which is why selecting on coverage selects on the outcome, and why a frame that looks complete should be interrogated rather than trusted. I reached this by auditing the frame first and letting the audit overturn my expectation, which is the discipline the question is testing.

## Check question 2

**Sample B produced no difference on this indicator. Explain why, then state the direction of bias for a survey-reported indicator.**

The recency rule selected all eight countries because every country's latest report is 2024, within three years of the frame maximum. A selection rule can only bias an estimate if it excludes something, and here it excluded nothing. The zero is not evidence that recency selection is harmless; it is evidence that the mechanism was smoothed over upstream by imputation.

On a survey-reported indicator the bias would run downward on stunting, meaning toward apparently better outcomes, for two reinforcing reasons. First, countries that field surveys regularly tend to have functioning statistics systems, which travel with stronger public administration and generally better social indicators. Second, and more importantly, countries in acute deterioration are exactly the countries where surveys are delayed or cancelled, because the same instability that raises stunting stops the enumeration. A recency filter therefore removes deteriorating situations at the moment they matter most. The bias is not neutral noise; it is a filter that deletes bad news. For indicators where a higher value is good, the same mechanism reverses the direction and produces apparent over-performance, which is why the rule to remember is not a sign but a sentence: recency selection excludes crisis, and crisis is the signal.

## Check question 3

**Name one place in the Binti Rising M&E data where the same bias could be operating now.**

The quarterly donor report compiles partners whose submissions arrive before the cut-off, and the Power BI milestone tracker defaults to excluding any partner with an incomplete submission for the period. In the last cycle at least one dispersed regional team submitted after the cut-off and its data rolled into the following quarter. If that team's lateness correlates with its operating difficulty, and in our programme the hardest-to-reach counties have the weakest connectivity and the highest staff turnover, then every on-time-only aggregate we publish understates caseload in precisely the counties the donor most wants to see. That is the better-performers sample in a uniform, applied nightly, by a dashboard setting rather than by a decision.

The fix I will put to the programme lead: publish the aggregate with a coverage footnote naming excluded partners and their share of expected beneficiaries, and show a bounded range, all-partners against on-time-only, rather than a single number. A range costs one line and removes the possibility that a filter silently becomes a finding.

*Internal verification note: the specific late-submission example above is drawn from my recollection of the last reporting cycle and must be checked against the cycle records before this answer is quoted externally. The structural claim, that on-time-only aggregation is a selection on reporting behaviour correlated with operating difficulty, holds regardless and is testable from the submission log.*
