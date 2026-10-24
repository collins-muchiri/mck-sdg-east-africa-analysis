"""Week 5: minimum detectable effect for a two-group comparison on the available panel."""
import numpy as np, pandas as pd, pathlib
from math import sqrt
df = pd.read_csv(pathlib.Path(__file__).resolve().parents[2] / "week01" / "week01_raw_sdg_2_2_1.csv")
r = df[df.year >= 2015]
sd = np.sqrt(np.mean([x.value.var(ddof=1) for _, x in r.groupby("country")]))
n = min(len(x) for _, x in r.groupby("country"))
print("sd", round(sd, 2), "n", n, "MDE", round((1.96 + 0.84) * sd * sqrt(2 / n), 2))
