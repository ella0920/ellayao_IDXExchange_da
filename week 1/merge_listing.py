import pandas as pd
import os

folder = 'raw_listing'
files = sorted([f for f in os.listdir(folder) if f.endswith('.csv')])

all_dfs = [pd.read_csv(os.path.join(folder, f), encoding='latin-1') for f in files]
final_df = pd.concat(all_dfs, ignore_index=True)

# Validation for Listings
print(f"Total Rows: {len(final_df)}")
print(final_df.columns.tolist())
print(final_df[['ListPrice', 'LivingArea', 'Bedrooms', 'Bathrooms']].describe())

final_df.to_csv('merged_listing.csv', index=False)
