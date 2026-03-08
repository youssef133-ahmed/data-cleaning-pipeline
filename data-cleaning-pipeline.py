import pandas as pd

# Load dataset
df = pd.read_csv("data/employees.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df = df.fillna("Unknown")

# Save cleaned data
df.to_csv("output/cleaned_employees.csv", index=False)

print("Data cleaned successfully")
