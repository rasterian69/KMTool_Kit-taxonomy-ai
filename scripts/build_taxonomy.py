import pandas as pd

# Load taxonomy CSV
df = pd.read_csv("../data/taxonomy.csv")

print("Loaded taxonomy:")
print(df.head())
