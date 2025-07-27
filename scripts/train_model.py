import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Simulasi data
data = pd.read_csv("data/metrics/sample.csv")
X = data[["cpu", "memory", "disk"]]

model = IsolationForest(contamination=0.05)
model.fit(X)

joblib.dump(model, "app/models/anomaly_model.pkl")
print("✅ Model trained and saved.")
