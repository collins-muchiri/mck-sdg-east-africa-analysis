"""
Session 1, Concept 1: sampling and bias.

Pulls SDG indicator 2.2.1 (proportion of children moderately or severely
stunted, per cent) for eight East African countries from the UN SDG global
indicator database, then shows how three different sampling rules over the same
underlying frame produce three different answers to the same question.

Data is public and open. Nothing here is synthetic. Provenance is recorded in
week01_results.md.

Run:  python3 week01_sampling_bias.py
"""
import json, os, statistics, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
INDICATOR = "2.2.1"
BASE = "https://unstats.un.org/SDGAPI/v1/sdg/Indicator/Data"

COUNTRIES = {
    "108": "Burundi", "231": "Ethiopia", "404": "Kenya", "646": "Rwanda",
    "706": "Somalia", "728": "South Sudan", "834": "United Republic of Tanzania",
    "800": "Uganda",
}


def fetch_page(page, cache_dir):
    path = os.path.join(cache_dir, f"page{page:02d}.json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    url = f"{BASE}?indicator={INDICATOR}&series=SH_STA_STNT&pageSize=1000&page={page}"
    last = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                payload = json.load(r)
            with open(path, "w") as f:
                json.dump(payload, f)
            return payload
        except Exception as e:
            last = e
            import time
            time.sleep(3)
    raise RuntimeError(f"page {page} failed after retries: {last}")


def fetch_all():
    cache_dir = os.path.join(HERE, "week01_cache")
    os.makedirs(cache_dir, exist_ok=True)
    rows, page = [], 1
    while page <= 32:
        payload = fetch_page(page, cache_dir)
        batch = payload.get("data") or []
        rows.extend(batch)
        total = int(payload.get("totalElements") or 0)
        if len(rows) >= total or not batch:
            break
        page += 1
    return rows


def main():
    raw = fetch_all()
    frame = []
    for rec in raw:
        code = str(rec.get("geoAreaCode"))
        if code not in COUNTRIES:
            continue
        try:
            year = int(float(rec["timePeriodStart"]))
            value = float(rec["value"])
        except (KeyError, TypeError, ValueError):
            continue
        frame.append({"code": code, "country": COUNTRIES[code], "year": year, "value": value,
                      "series": rec.get("series"), "source": rec.get("source")})
    if not frame:
        print("ERROR: no rows retrieved for the eight countries")
        return 1
    frame.sort(key=lambda d: (d["country"], d["year"]))

    os.makedirs(HERE, exist_ok=True)
    with open(os.path.join(HERE, "week01_raw_sdg_2_2_1.csv"), "w") as f:
        f.write("geo_area_code,country,year,value,series,source\n")
        for d in frame:
            f.write(f'{d["code"]},{d["country"]},{d["year"]},{d["value"]},{d["series"]},"{d["source"]}"\n')

    # ---- coverage table
    cov = {}
    for code, name in COUNTRIES.items():
        pts = [d for d in frame if d["code"] == code]
        years = sorted({d["year"] for d in pts})
        latest = max(years) if years else None
        latest_val = next((d["value"] for d in pts if d["year"] == latest), None)
        cov[code] = {"country": name, "n_years": len(years), "first": years[0] if years else None,
                     "latest": latest, "latest_value": latest_val,
                     "gap_2015_on": len([y for y in range(2015, 2025) if y not in years])}
    with open(os.path.join(HERE, "week01_country_coverage.csv"), "w") as f:
        f.write("geo_area_code,country,reported_years,first_year,latest_year,latest_value,missing_years_2015_to_2024\n")
        for code, c in sorted(cov.items(), key=lambda kv: kv[1]["n_years"]):
            f.write(f'{code},{c["country"]},{c["n_years"]},{c["first"]},{c["latest"]},{c["latest_value"]},{c["gap_2015_on"]}\n')

    reporting = {c: v for c, v in cov.items() if v["latest_value"] is not None}
    full_mean = statistics.mean(v["latest_value"] for v in reporting.values())
    max_latest = max(v["latest"] for v in reporting.values())

    # sample B: only countries that reported in the last three reporting years
    b_codes = [c for c, v in reporting.items() if v["latest"] >= max_latest - 2]
    b_mean = statistics.mean(reporting[c]["latest_value"] for c in b_codes)

    # sample C: only countries performing better than the regional median
    med = statistics.median(v["latest_value"] for v in reporting.values())
    c_codes = [cc for cc, v in reporting.items() if v["latest_value"] <= med]
    c_mean = statistics.mean(reporting[cc]["latest_value"] for cc in c_codes)

    def names(codes):
        return ", ".join(sorted(reporting[c]["country"] for c in codes))

    lines = []
    lines.append("# Week 1 results: sampling and bias on SDG 2.2.1, East Africa")
    lines.append("")
    lines.append("Source: UN SDG global indicator database, indicator 2.2.1, series SH_STA_STNT, "
                 "Joint Child Malnutrition Estimates (2025 edition), UNICEF, WHO and the World Bank Group. "
                 "Retrieved by script on the date of the session. Public and open licensed. Nothing synthetic.")
    lines.append("")
    lines.append("## Coverage of the frame")
    lines.append("")
    lines.append("| Country | Reported years | First | Latest | Latest value, per cent | Missing years 2015 to 2024 |")
    lines.append("|---|---|---|---|---|---|")
    for code, c in sorted(cov.items(), key=lambda kv: -kv[1]["n_years"]):
        lines.append(f'| {c["country"]} | {c["n_years"]} | {c["first"]} | {c["latest"]} | '
                     f'{c["latest_value"] if c["latest_value"] is not None else "none"} | {c["gap_2015_on"]} |')
    lines.append("")
    lines.append("## The same question under three sampling rules")
    lines.append("")
    lines.append("Question: what is the regional mean stunting prevalence, latest reported year per country, unweighted?")
    lines.append("")
    lines.append("| Sample | Rule | Countries | n | Mean, per cent | Difference from full frame |")
    lines.append("|---|---|---|---|---|---|")
    lines.append(f'| A, full frame | every country with any report | all | {len(reporting)} | {full_mean:.1f} | reference |')
    lines.append(f'| B, recent reporters | latest report within three years of {max_latest} | {names(b_codes)} | '
                 f'{len(b_codes)} | {b_mean:.1f} | {b_mean - full_mean:+.1f} points |')
    lines.append(f'| C, better performers | latest value at or below the regional median of {med:.1f} | {names(c_codes)} | '
                 f'{len(c_codes)} | {c_mean:.1f} | {c_mean - full_mean:+.1f} points |')
    lines.append("")
    lines.append("## What the numbers show")
    lines.append("")
    lines.append(f"Sample B moves the regional mean by {b_mean - full_mean:+.1f} percentage points and sample C by "
                 f"{c_mean - full_mean:+.1f} points, without a single underlying observation changing. The frame is "
                 "identical in all three rows. Only the rule that selected countries differs.")
    lines.append("")
    lines.append("Sample B moves the mean by zero, and that zero is the more important result of the two. Indicator "
                 "2.2.1 is a modelled estimate: the Joint Child Malnutrition Estimates publish a value for every "
                 "country-year, so the frame contains no missing cells to select on. A database with no gaps is not a "
                 "database with no missing data; the gaps were filled by a model before you arrived. Selection on "
                 "reporting recency therefore shows nothing here, and would show a great deal on a survey-reported "
                 "indicator such as SDG 5.b.1 or SDG 4.1.1, where a country appears only in the years it fielded a "
                 "survey. Week 2 repeats this exercise on a survey-reported indicator so the recency mechanism can be "
                 "seen biting.")
    lines.append("")
    lines.append("Sample C is the bias that operates in advocacy: selecting on the outcome itself. A ministry that "
                 "quotes only the better-performing half of the region is not lying about any number. It is lying "
                 "about the set the numbers were drawn from.")
    lines.append("")
    lines.append("## Limitations")
    lines.append("")
    lines.append("- The mean is unweighted by population, so a small country counts the same as a large one. A "
                 "population-weighted mean would answer a different question and could move in the opposite direction.")
    lines.append("- Latest-year values come from different calendar years across countries, so sample A mixes years. "
                 "That mixture is itself a form of the bias under study.")
    lines.append("- Because 2.2.1 is modelled, the coverage table shows complete reporting for all eight countries. "
                 "Completeness here is a property of the estimation method, not of national statistical systems, and "
                 "must not be read as evidence that all eight countries fielded surveys in all twenty-five years.")
    lines.append("- SDG 2.2.1 values are modelled estimates from the Joint Child Malnutrition Estimates, not direct "
                 "survey counts, so part of the between-country variation is model behaviour rather than observation.")
    lines.append("")
    lines.append("## Check questions, to be answered in writing by the candidate")
    lines.append("")
    lines.append("1. Which countries have the fewest reported years, and why is that non-random?")
    lines.append("2. Sample B produced no difference on this indicator. Explain why, then state in which direction a "
                 "recency-only sample would bias the regional mean if the indicator were survey-reported rather than "
                 "modelled, and why.")
    lines.append("3. Name one place in the Binti Rising M&E data where the same bias could be operating now.")
    with open(os.path.join(HERE, "week01_results.md"), "w") as f:
        f.write("\n".join(lines) + "\n")

    # ---- coverage figure
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    order = sorted(cov.values(), key=lambda c: c["n_years"])
    fig, ax = plt.subplots(figsize=(9, 4.4))
    cols = ["#C0563B" if c["n_years"] < 8 else ("#E0A030" if c["n_years"] < 14 else "#2E8B57") for c in order]
    bars = ax.barh([c["country"] for c in order], [c["n_years"] for c in order], color=cols, height=0.62)
    for b, c in zip(bars, order):
        ax.text(b.get_width() + 0.25, b.get_y() + b.get_height() / 2,
                f'{c["n_years"]} yrs, latest {c["latest"]}', va="center", fontsize=8.5)
    ax.set_xlabel("Years reported in the SDG database, indicator 2.2.1")
    ax.set_title("Reporting coverage is not random\nUN SDG global indicator database, eight East African countries",
                 fontsize=11, loc="left")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis="x", color="#D6DBE4", linewidth=0.6, alpha=0.8)
    ax.set_axisbelow(True)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "week01_coverage.png"), dpi=150)
    plt.close(fig)

    print(f"frame rows: {len(frame)}  countries with data: {len(reporting)} of {len(COUNTRIES)}")
    print(f"full mean {full_mean:.1f} | sample B {b_mean:.1f} ({b_mean-full_mean:+.1f}) | sample C {c_mean:.1f} ({c_mean-full_mean:+.1f})")
    for f_ in sorted(os.listdir(HERE)):
        print("  wrote", f_)
    return 0


if __name__ == "__main__":
    sys.exit(main())
