# Week 1 training pack: teaching sampling and bias to programme and data teams

Facilitator guide. Built from the week 1 build in this folder so that any trainer can deliver the session without the original author present.
Licence: MIT, attribution to Muchiri Collins Kamama. Reuse, adapt and teach freely.

## Audience and prerequisites

M&E officers, data analysts, programme managers and junior data scientists in NGOs, UN agencies, county governments or consultancies. No statistics background required. Prerequisites: comfort with a spreadsheet, and access to a laptop if the hands-on variant is run. Duration 90 minutes. Maximum useful cohort 20.

## Learning objectives

By the end of the session participants can:
1. Distinguish selection bias, coverage bias and missingness, and give a programme example of each.
2. Explain why a complete-looking database can still carry bias, including bias introduced by upstream imputation.
3. Compute how a sampling rule changes an aggregate, using the files in this folder.
4. State the direction of bias a given selection rule introduces, not merely its existence.
5. Write a coverage disclosure footnote for a report that excludes late or incomplete submissions.

## Materials

- week01_sampling_bias.py, the reproducible pull and analysis
- week01_raw_sdg_2_2_1.csv, 1,200 country-year observations
- week01_country_coverage.csv, the coverage audit
- week01_results.md, tables and narrative
- week01_coverage.png, the coverage figure
- week01_note_and_answers.md, the worked note and model answers, for facilitator reference only; do not distribute before the exercise

## Session plan, 90 minutes

| Minutes | Activity |
|---|---|
| 0 to 10 | Provocation. Show one number on screen: 23.2 per cent. Ask what it could be. Then show 30.2 per cent and ask which is the regional stunting mean. Both are. Reveal that the only difference is a filter. |
| 10 to 25 | Concept. The three names: selection, coverage, missingness. Worked definitions with programme examples. Emphasise that representative describes a selection mechanism, not a table of summaries. |
| 25 to 50 | Hands-on. Participants run or walk through week01_sampling_bias.py, open week01_country_coverage.csv and reproduce the three-sample table by hand in a spreadsheet from the raw CSV. The hand reproduction is the point; it forces them to touch the frame. |
| 50 to 65 | The twist. Reveal that sample B moved nothing and ask why before explaining. Then explain modelled estimates and imputed completeness. This is the segment participants remember. |
| 65 to 80 | Direction of bias. Small groups state the direction for three rules: recency on a survey indicator, better-performers-only, and excluding partners with incomplete submissions. Groups report in one sentence each. |
| 80 to 90 | Disclosure practice. Each participant drafts a two-line coverage footnote for a report of their own that excludes something. Two are read aloud and critiqued. |

## The two traps, and how to handle them

Trap one: participants expect the recency sample to move the number, and when it does not they assume a coding error. Let them debug for five minutes before revealing that the data is modelled. The debugging detour is where the imputation lesson lands.

Trap two: participants read the complete coverage table as evidence of good data quality. Redirect with one question: who produced these values, an enumerator or a model? Then ask what a model fills gaps with. Silence is acceptable; the question is the teaching.

## Common wrong answers and the redirect

| Wrong answer | Redirect question |
|---|---|
| The database is complete so there is no bias. | Complete according to whom? Who produced the cells that no survey generated? |
| Bigger samples fix this. | Does a bigger sample drawn by the same rule fix the rule? |
| We should just include every partner regardless of data quality. | What does including a partner with zero verified records do to the mean, and who bears that error? |
| The seven-point gap means someone manipulated data. | Every retained record is valid. What changed, the records or the set? |
| Weighting solves selection bias. | Weighting solves what, exactly, and what does it need that selection on the outcome destroys? |

## Exercise variants

1. Recency made visible. Repeat the build with SDG 5.b.1, mobile phone ownership by sex, or SDG 4.1.1, learning outcomes. Participants compare the coverage tables and explain why the recency rule now bites. Ninety minutes, includes the pull.
2. Weighting. Recompute the three means weighted by national population under five, using a public UN population prospect extract. Discuss when weighting helps and when it cannot.
3. Their own data. Each participant audits one aggregate they publish: list what is excluded, why, and the suspected direction of bias. Deliverable is the two-line disclosure footnote. This variant has produced process changes in every cohort where it has been run, because it moves the lesson from a public database onto the participant's own desk.

## Assessment rubric for the note and answers

| Level | Descriptor |
|---|---|
| Developing | Defines bias but treats completeness as safety. Cannot state a direction. |
| Competent | Distinguishes the three mechanisms, reproduces the table, states direction for one rule. |
| Strong | Explains the imputation twist without prompting, states direction with the causal chain, proposes disclosure rather than cleaning as the remedy. |
| Exceptional | Additionally identifies that the unweighted mean mixes calendar years, and proposes the bounded-range reporting format. |

The candidate submission in week01_note_and_answers.md sits at Exceptional on this rubric and may be used as the worked exemplar after participants have attempted their own.

## Slide outline, eight slides

1. Two numbers, one frame: 30.2 and 23.2.
2. A dataset is a picture of a process.
3. The three names: selection, coverage, missingness.
4. The build: eight countries, 1,200 observations, three rules.
5. The table: full, recency, better-performers.
6. The twist: modelled estimates and imputed completeness.
7. Direction of bias: recency excludes crisis, and crisis is the signal.
8. The remedy is disclosure: what was excluded, why, and which way it pushes.

## Adaptation for non-technical audiences

Drop the hands-on block and replace it with a paper exercise: give each table of six participants eight cards with country names and values, ask two tables to compute the mean of all eight and the other four tables to compute the mean of their four best cards, then compare on a whiteboard. The physical act of setting cards aside teaches selection better than any slide.
