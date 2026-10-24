# mck-sdg-east-africa-analysis

Applied statistical analysis of public United Nations SDG data for East Africa. Portfolio artifact 1 of 3, built in public as part of a 24-week learning programme.

## The problem

One decision-oriented question: does the reported regional mean of child stunting prevalence in East Africa depend on which countries you include, and by how much? A donor reading a regional average is reading a sampling decision, usually an invisible one.

## Data

UN SDG global indicator database, indicator 2.2.1, series SH_STA_STNT, Joint Child Malnutrition Estimates 2025 edition (UNICEF, WHO, World Bank Group). Retrieved by script on 24 October 2026. Public and open. Eight M49 geo areas: Burundi 108, Ethiopia 231, Kenya 404, Rwanda 646, Somalia 706, South Sudan 728, Tanzania 834, Uganda 800. Nothing synthetic.

## Method

1. Pull every country-year observation for the eight codes, with paging, caching and retries.
2. Audit coverage: reported years, first and latest year, missing years 2015 to 2024.
3. Draw three samples from the identical frame: all reporters; recent reporters only; better performers only.
4. Compute the unweighted regional mean of latest-year values under each rule and tabulate the difference.

## How to run

    python3 analysis/week01_sampling_bias.py

Needs network access to unstats.un.org. Writes data/, docs/ and figures/ in place. Page cache lives in week01_cache/ and is gitignored.

## Findings

| Sample | Rule | n | Mean, per cent | Difference |
|---|---|---|---|---|
| A | full frame | 8 | 30.2 | reference |
| B | recent reporters only | 8 | 30.2 | +0.0 |
| C | better performers only | 4 | 23.2 | -7.0 |

Sample C moves the regional mean seven percentage points by dropping four countries, with no underlying observation changed. Sample B moves it not at all, and that zero is the more important result: 2.2.1 is a modelled estimate, so every country-year cell is populated and recency selection has nothing to select on. Completeness here is a property of the estimation method, not of national statistical systems. See docs/week01_results.md for the full narrative.

## Limitations

Unweighted mean, so a small country counts the same as a large one. Latest-year values fall in different calendar years across countries. Values are modelled estimates, not direct survey counts. A survey-reported indicator is needed to make recency selection visible; that is week 2 of the programme.

## Licence

MIT. See LICENSE.
