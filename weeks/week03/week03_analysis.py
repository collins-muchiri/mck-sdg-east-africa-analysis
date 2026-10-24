"""Week 3: pooled versus within-country correlation, the confounder is country."""
import numpy as np, pandas as pd, pathlib
df = pd.read_csv(pathlib.Path(__file__).resolve().parents[2] / "week01" / "week01_raw_sdg_2_2_1.csv")
print("pooled", round(np.corrcoef(df.year, df.value)[0, 1], 3))
for c, s in df.groupby("country"):
    print(c, round(np.corrcoef(s.year, s.value)[0, 1], 3))
