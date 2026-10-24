"""Week 2: two-sample comparison with a bootstrap interval. Serial correlation noted, not hidden."""
import numpy as np, pandas as pd, pathlib
df = pd.read_csv(pathlib.Path(__file__).resolve().parents[2] / "week01" / "week01_raw_sdg_2_2_1.csv")
a = df[df.country == "Kenya"].value.to_numpy(); b = df[df.country == "Burundi"].value.to_numpy()
rng = np.random.default_rng(7); d = [b[rng.integers(0, len(b), len(b))].mean() - a[rng.integers(0, len(a), len(a))].mean() for _ in range(4000)]
print("difference", round(b.mean() - a.mean(), 1), "ci95", [round(x, 1) for x in np.percentile(d, [2.5, 97.5])])
