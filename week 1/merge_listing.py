import pandas as pd
import os

# Merging all csv files
folder = 'raw_listing'
files = sorted([f for f in os.listdir(folder) if f.endswith('.csv')])
all_dfs = []
all_dfs = []
total_raw_rows = 0

# Read row count of each file and append to a list
print("--- Individual File Row Counts ---")
for f in files:
    df = pd.read_csv(os.path.join(folder, f), encoding='latin-1')
    current_rows = len(df)
    print(f"Row count for {f}: {current_rows}")
    total_raw_rows += current_rows
    all_dfs.append(df)

# Total rows before concatenation
print(f"\nTotal sum of individual files (Before Concatenation): {total_raw_rows}")

# Concatenate all df and check total row count before filtering
final_df = pd.concat(all_dfs, ignore_index=True)
print("\n--- Before Filter Validation ---")
print(f"Total Rows Before Filter: {len(final_df)}")

# Row counts of each property type
print("\nProperty Types before filter:")
print(final_df['PropertyType'].value_counts())

# Row counts of residential type
residential_df = final_df[final_df['PropertyType'] == 'Residential']
print("\n--- After Filter Validation ---")
print(f"Total Rows After Filter: {len(residential_df)}")
print("\nProperty Types after filter:")
print(residential_df['PropertyType'].value_counts())

# ==========================================
# VALIDATION COMMENTS
# ==========================================
# Row count BEFORE concatenation: 852963
# Row count AFTER concatenation: 852963
# Row count BEFORE Residential filter: 852963
# Row count AFTER Residential filter: 540183
# ==========================================

residential_df.to_csv('merged_listing.csv', index=False)
