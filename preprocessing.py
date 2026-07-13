import pandas as pd

# Load Dataset
df = pd.read_csv("student_performance_dataset.csv")

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

print("\nShape After Cleaning:")
print(df.shape)

# Save cleaned dataset
df.to_csv(
    "cleaned_student_performance_dataset.csv",
    index=False
)

print("\nCleaned Dataset Saved Successfully!")