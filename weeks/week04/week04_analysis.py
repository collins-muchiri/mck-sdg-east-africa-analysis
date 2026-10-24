"""Week 4: year trend with country fixed effects plus residual diagnostics. Cluster-robust errors required before quoting intervals."""
import numpy as np, pandas as pd, pathlib
df = pd.read_csv(pathlib.Path(__file__).resolve().parents[2] / "week01" / "week01_raw_sdg_2_2_1.csv")
X = pd.get_dummies(df[["year", "country"]], columns=["country"], dtype=float)
cols = [c for c in X.columns if c != "country_" + sorted(df.country.unique())[0]]
A = np.column_stack([X[cols].to_numpy(), np.ones(len(df))]); y = df.value.to_numpy()
beta, *_ = np.linalg.lstsq(A, y, rcond=None)
print("year coefficient", round(beta[cols.index("year")], 3))
