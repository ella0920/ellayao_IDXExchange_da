import pandas as pd

# Read in the data
sold = pd.read_csv('merged_sold.csv', low_memory=False)

# Identify number of rows and columns
print("--- Dataset Shape ---")
print(sold.shape)

# Inspect structure
print("\n--- First 5 Rows ---")
print(sold.head())
print(sold.columns)

# Check property categories
print("\n--- Unique Property Types ---")
print(sold['PropertyType'].unique())

# Validate completeness
print("\n--- Null Counts ---")
print(sold.isnull().sum())

# Columns with >90% missing values
missing_percentages = sold.isnull().mean() * 100
high_missing_cols = missing_percentages[missing_percentages > 90]
print("\n--- Columns with >90% Missing Values ---")
print(high_missing_cols)

# Numeric distribution review
core_numeric = ['ClosePrice', 'LivingArea', 'DaysOnMarket', 'YearBuilt']
print("\n--- Numeric Distribution Summary ---")
print(sold[core_numeric].describe())

cols_to_drop = high_missing_cols.index.tolist()
sold_cleaned = sold.drop(columns=cols_to_drop)

# Data cleaning
initial_count = len(sold)
print(f"\nFiltering Summary:")
print(f"- Property filtering: {initial_count} rows confirmed.")
print(f"- Column filtering: Dropped {len(cols_to_drop)} columns with >90% missing values.")
print(f"- Final dataset shape: {sold_cleaned.shape}")

sold_cleaned.to_csv('filtered_residential_data.csv', index=False)

# ====== EDA Summary ======
# --- Dataset shape ---
# (397603, 84) 
# Total rows: 397603
# Total Columns: 84
#
# --- Unique property type ---
# ['Residential']
#
# --- Columns with >90% missing values ---
# 17 columns:
# BuilderName                      95.083790
# TaxYear                         100.000000
# BuildingAreaTotal                93.009862
# ElementarySchoolDistrict        100.000000
# CoBuyerAgentFirstName            90.938952
# BelowGradeFinishedArea           99.424049
# BusinessType                    100.000000
# CoveredSpaces                   100.000000
# LotSizeDimensions                95.140630
# MiddleOrJuniorSchoolDistrict    100.000000
# OriginatingSystemName            90.127841
# OriginatingSystemSubName         90.127841
