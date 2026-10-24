"""Week 6: difference-in-differences laid out with its parallel-trends plot and a stated failure. Teaching design, not a causal claim."""
import pandas as pd, pathlib
df = pd.read_csv(pathlib.Path(__file__).resolve().parents[2] / "week01" / "week01_raw_sdg_2_2_1.csv")
tr = df[df.country == "Kenya"].set_index("year").value
ctrl = df[df.country != "Kenya"].groupby("year").value.mean()
pre, post = slice(2008, 2012), slice(2013, 2024)
print("DiD", round((tr.loc[post].mean() - tr.loc[pre].mean()) - (ctrl.loc[post].mean() - ctrl.loc[pre].mean()), 2))
