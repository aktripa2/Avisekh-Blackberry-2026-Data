import pandas as pd

# ==========================
# Load Excel File
# ==========================

df = pd.read_excel(
    "Master_Reflectance_Data2.xlsx"
)

print("="*60)
print("DATASET INFORMATION")
print("="*60)

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

# ==========================
# Missing Values
# ==========================

print("\n"+"="*60)
print("MISSING VALUES")
print("="*60)

print(df.isnull().sum())

# ==========================
# Harvest Status Count
# ==========================

print("\n"+"="*60)
print("HARVEST STATUS")
print("="*60)

print(df["Harvest_Status"].value_counts())

# ==========================
# Cultivar Count
# ==========================

print("\n"+"="*60)
print("CULTIVAR COUNT")
print("="*60)

print(df["Cultivar"].value_counts())

# ==========================
# Date Count
# ==========================

print("\n"+"="*60)
print("DATE COUNT")
print("="*60)

print(df["Date"].value_counts())

# ==========================
# Row Count
# ==========================

print("\n"+"="*60)
print("ROW COUNT")
print("="*60)

print(df["Row_No"].value_counts())

# ==========================
# Duplicate Check
# ==========================

print("\n"+"="*60)
print("DUPLICATES")
print("="*60)

duplicates = df.duplicated().sum()

print("Total duplicate rows =", duplicates)

# ==========================
# Summary Statistics
# ==========================

bands = [
    410,435,460,485,510,535,
    560,585,610,645,680,705,
    730,760,810,860,900,940
]

print("\n"+"="*60)
print("SUMMARY STATISTICS")
print("="*60)

print(df[bands].describe())

print("\nDataset check completed successfully!")