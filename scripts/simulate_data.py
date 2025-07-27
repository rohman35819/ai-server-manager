import psutil
import pandas as pd
import time

records = []

for _ in range(10):
    record = {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    }
    records.append(record)
    time.sleep(1)

df = pd.DataFrame(records)
df.to_csv("data/metrics/sample.csv", index=False)
print("✅ Data saved to sample.csv")
