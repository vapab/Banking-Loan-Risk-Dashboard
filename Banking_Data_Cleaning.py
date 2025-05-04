#Fix missing Issue_date column

import pandas as pd

# Load the file
file_path = r"path"
df = pd.read_csv(file_path, low_memory=False)

# Always ensure 'issue_month' column exists, even if it's null
if 'issue_month' not in df.columns:
    df['issue_month'] = pd.NA

# Create date-based columns from issue_d
if 'issue_d' in df.columns:
    df['issue_d'] = pd.to_datetime(df['issue_d'], format='%b-%y', errors='coerce')

    # Monthly period (YYYY-MM)
    df['issue_month_real'] = df['issue_d'].dt.to_period('M').astype(str)

    # Full month name (e.g., January)
    df['issue_month_name'] = df['issue_d'].dt.strftime('%B')

    # Year only
    df['issue_year'] = df['issue_d'].dt.year

    print("Created 'issue_month_real', 'issue_month_name', and 'issue_year' from 'issue_d'.")
else:
    print("'issue_d' column not found. Skipping date column creation.")

# Save to a new file
output_path = r"path"
df.to_csv(output_path, index=False)

print("Saved file to:")
print(output_path)

#Find discrepancies by ID column value

# import pandas as pd
# import numpy as np

# # ── CONFIG ─────────────────────────────────────────────
# CSV_PATH = r"path"
# CHUNK    = 50_000        
# LOOKUP_ID = 68_407_277   
# # ───────────────────────────────────────────────────────

# # Running counters
# total_rows   = 0
# null_count   = 0          # NaN or blank
# numeric_count = 0         # parses cleanly to float/int
# string_count  = 0         # non‑numeric leftovers

# lookup_row = None         # store row when we meet the ID

# cols_needed = ["loan_amnt", "member_id", "id"]

# for chunk in pd.read_csv(CSV_PATH,
#                          usecols=cols_needed,
#                          chunksize=CHUNK,
#                          dtype=str,          # read as strings so we can test type
#                          low_memory=False):

#     total_rows += len(chunk)

#     # --- 1. classify each loan_amnt entry -----------------
#     loan_series = chunk["loan_amnt"].str.strip()

#     is_null        = loan_series.isna() | (loan_series == "")
#     is_numeric     = pd.to_numeric(loan_series, errors="coerce").notna() & ~is_null
#     is_string_bad  = ~is_null & ~is_numeric     # anything else (e.g., "N/A")

#     null_count    += is_null.sum()
#     numeric_count += is_numeric.sum()
#     string_count  += is_string_bad.sum()

#     # --- 2. look up the member_id you asked for ----------
#     match = chunk.loc[chunk["id"] == str(LOOKUP_ID)]
#     if not match.empty:
#         lookup_row = match.iloc[0]

# # ── OUTPUT ─────────────────────────────────────────────
# print("=== loan_amnt data‑type profile ===")
# print(f" Total rows:               {total_rows:,}")
# print(f" Numeric values:         {numeric_count:,}")
# print(f" Null / blank values:    {null_count:,}")
# print(f" Non‑numeric strings:    {string_count:,}")

# print("\n=== Lookup for member_id", LOOKUP_ID, "===")
# if lookup_row is not None:
#     print(lookup_row[["member_id", "loan_amnt"]])
# else:
#     print("member_id not found in file.")


## Copy Column for large dataset excel
#import pandas as pd

# # Load the file
# file_path = r"path"
# df = pd.read_csv(file_path, low_memory=False)

# # Duplicate 'loan_amnt_fixed' into new 'loan_amnt' column
# df['loan_amnt'] = df['loan_amnt_new']

# # Save to a new file keeping both columns
# output_path = r"path"
# df.to_csv(output_path, index=False)

# print("Saved file with both 'loan_amnt_fixed' and 'loan_amnt' to:")
# print(output_path)


