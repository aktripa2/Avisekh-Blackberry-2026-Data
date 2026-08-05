# ============================================================
# BLACKBERRY SPECTRAL ANALYSIS
# Exploratory Data Analysis (EDA)
# Author: Avisekh Kumar Tripathy
# ============================================================

import os
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# Create Results Folder
# ============================================================

os.makedirs("Results/EDA", exist_ok=True)

# ============================================================
# Load Dataset
# ============================================================

df = pd.read_excel("Master_Reflectance_Data2.xlsx")

# ============================================================
# Spectral Bands
# ============================================================

bands = [
    410,435,460,485,510,535,
    560,585,610,645,680,705,
    730,760,810,860,900,940
]

# ============================================================
# DATASET SUMMARY
# ============================================================

print("="*60)
print("DATASET SUMMARY")
print("="*60)

print("\nShape :", df.shape)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows :", df.duplicated().sum())

print("\nHarvest Status")
print(df["Harvest_Status"].value_counts())

print("\nCultivar")
print(df["Cultivar"].value_counts())

print("\nDates")
print(df["Date"].value_counts())

print("\nRows")
print(df["Row_No"].value_counts())

# ============================================================
# SUMMARY STATISTICS
# ============================================================

summary = df[bands].describe()

summary.to_excel(
    "Results/EDA/Summary_Statistics.xlsx"
)

print("\nSummary Statistics Saved.")

# ============================================================
# CORRELATION MATRIX
# ============================================================

corr = df[bands].corr()

corr.to_excel(
    "Results/EDA/Correlation_Matrix.xlsx"
)

print("Correlation Matrix Saved.")

# ============================================================
# FIGURE 1
# Harvest Distribution
# ============================================================

plt.figure(figsize=(6,5))

counts = df["Harvest_Status"].value_counts()

plt.bar(
    counts.index,
    counts.values
)

for i,v in enumerate(counts.values):
    plt.text(i,v+5,str(v),ha='center')

plt.title("Harvest Status Distribution")
plt.xlabel("Harvest Status")
plt.ylabel("Number of Berries")

plt.tight_layout()

plt.savefig(
    "Results/EDA/Harvest_Distribution.png",
    dpi=300
)

plt.show()

# ============================================================
# FIGURE 2
# Cultivar Distribution
# ============================================================

plt.figure(figsize=(6,5))

counts = df["Cultivar"].value_counts()

plt.bar(
    counts.index,
    counts.values
)

for i,v in enumerate(counts.values):
    plt.text(i,v+5,str(v),ha='center')

plt.title("Cultivar Distribution")
plt.xlabel("Cultivar")
plt.ylabel("Number of Berries")

plt.tight_layout()

plt.savefig(
    "Results/EDA/Cultivar_Distribution.png",
    dpi=300
)

plt.show()

# ============================================================
# FIGURE 3
# Mean Spectrum
# Before vs After
# ============================================================

before = df[
    df["Harvest_Status"]=="Before Harvesting"
][bands].mean()

after = df[
    df["Harvest_Status"]=="After Harvesting"
][bands].mean()

plt.figure(figsize=(8,5))

plt.plot(
    bands,
    before,
    marker='o',
    linewidth=2,
    label="Before Harvest"
)

plt.plot(
    bands,
    after,
    marker='s',
    linewidth=2,
    label="After Harvest"
)

plt.xlabel("Wavelength (nm)")
plt.ylabel("Mean Reflectance")
plt.title("Mean Reflectance Spectrum")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "Results/EDA/Mean_Harvest.png",
    dpi=300
)

plt.show()

# ============================================================
# FIGURE 4
# Mean Spectrum by Cultivar
# ============================================================

plt.figure(figsize=(8,5))

for cultivar in df["Cultivar"].unique():

    spectrum = df[
        df["Cultivar"]==cultivar
    ][bands].mean()

    plt.plot(
        bands,
        spectrum,
        marker='o',
        linewidth=2,
        label=cultivar
    )

plt.xlabel("Wavelength (nm)")
plt.ylabel("Mean Reflectance")

plt.title("Mean Spectrum of Blackberry Cultivars")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "Results/EDA/Mean_Cultivar.png",
    dpi=300
)

plt.show()

# ============================================================
# FIGURE 5
# Boxplots
# ============================================================

plt.figure(figsize=(14,6))

df[bands].boxplot()

plt.title("Reflectance Distribution Across Wavelengths")

plt.xlabel("Wavelength (nm)")
plt.ylabel("Reflectance")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "Results/EDA/Boxplots.png",
    dpi=300
)

plt.show()

# ============================================================
# FIGURE 6
# Correlation Heatmap
# ============================================================

plt.figure(figsize=(10,8))

plt.imshow(
    corr,
    interpolation='nearest',
    aspect='auto'
)

plt.colorbar(label="Correlation")

plt.xticks(
    range(len(bands)),
    bands,
    rotation=90
)

plt.yticks(
    range(len(bands)),
    bands
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    "Results/EDA/Correlation_Heatmap.png",
    dpi=300
)

plt.show()

# ============================================================
# Finished
# ============================================================

print("\n")
print("="*60)
print("EDA COMPLETED SUCCESSFULLY")
print("="*60)

print("\nAll figures saved to:")

print("Results/EDA/")