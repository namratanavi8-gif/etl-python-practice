# =====================================================
# 🚀 COMPLETE ETL DATA VALIDATION - NAMRATA
# =====================================================
# HOW TO RUN:
# 1. Go to https://colab.research.google.com
# 2. Click "New Notebook"
# 3. Copy paste this entire code
# 4. Click ▶️ Run
# NO FILE UPLOAD NEEDED - Data is already inside!
# =====================================================

import pandas as pd
from io import StringIO

# =====================================================
# 📂 SOURCE DATA (17 Records)
# =====================================================
source_csv = """customer_id,customer_name,city,product,quantity,price,order_date
C001,Namrata,Bangalore,Laptop,1,55000,2024-01-10
C002,Ravi,Mumbai,Mobile,2,15000,2024-01-11
C003,Priya,Delhi,Tablet,1,25000,2024-01-12
C004,Suresh,Chennai,Laptop,1,60000,2024-01-13
C005,Anjali,Pune,Mobile,3,12000,2024-01-14
C006,Kiran,Hyderabad,Headphones,2,3000,2024-01-15
C007,Deepa,Bangalore,Tablet,1,22000,2024-01-16
C008,Mahesh,Mumbai,Laptop,2,55000,2024-01-17
C009,Sneha,Delhi,Mobile,1,18000,2024-01-18
C010,Arun,Chennai,Headphones,3,3000,2024-01-19
C011,Mallikarjun,Bangalore,Laptop,2,55000,2024-01-20
C012,Pavitra,Mysore,Mobile,1,20000,2024-01-21
C013,Lokesh,Hubli,Tablet,2,25000,2024-01-22
C014,Saroja,Belgaum,Headphones,1,3000,2024-01-23
C015,Chandrashekhar,Dharwad,Laptop,1,62000,2024-01-24
C016,Virat,Bangalore,Mobile,2,18000,2024-01-25
C017,Saku,Mangalore,Tablet,1,23000,2024-01-26"""

# =====================================================
# 📂 TARGET DATA (16 Records + 1 Duplicate = 17 rows)
# =====================================================
target_csv = """customer_id,customer_name,city,product,quantity,price,order_date
C001,Namrata,Bangalore,Laptop,1,55000,2024-01-10
C002,Ravi,Mumbai,Mobile,2,15000,2024-01-11
C003,Priya,Delhi,Tablet,1,25000,2024-01-12
C004,Suresh,Chennai,Laptop,1,60000,2024-01-13
C005,Anjali,Pune,Mobile,3,12000,2024-01-14
C006,Kiran,Hyderabad,Headphones,2,3000,2024-01-15
C007,Deepa,Bangalore,Tablet,1,22000,2024-01-16
C008,Mahesh,Mumbai,Laptop,2,55000,2024-01-17
C011,Mallikarjun,Bangalore,Laptop,2,55000,2024-01-20
C012,Pavitra,Mysore,Mobile,1,20000,2024-01-21
C013,Lokesh,Hubli,Tablet,2,25000,2024-01-22
C014,Saroja,Belgaum,Headphones,1,3000,2024-01-23
C015,Chandrashekhar,Dharwad,Laptop,1,62000,2024-01-24
C016,Virat,Bangalore,Mobile,2,18000,2024-01-25
C017,Saku,Mangalore,Tablet,1,23000,2024-01-26
C001,Namrata,Bangalore,Laptop,1,55000,2024-01-10"""

# Load data into pandas
source = pd.read_csv(StringIO(source_csv))
target = pd.read_csv(StringIO(target_csv))


# =====================================================
# STEP 1 - VIEW DATA
# =====================================================
print("=" * 50)
print("📂 STEP 1 - SOURCE DATA")
print("=" * 50)
print(source.to_string(index=False))

print("\n" + "=" * 50)
print("📂 STEP 1 - TARGET DATA")
print("=" * 50)
print(target.to_string(index=False))


# =====================================================
# STEP 2 - COUNT CHECK
# =====================================================
print("\n" + "=" * 50)
print("🔢 STEP 2 - COUNT CHECK")
print("=" * 50)

source_count = len(source)
target_count = len(target)

print(f"Source Record Count : {source_count}")
print(f"Target Record Count : {target_count}")

if source_count == target_count:
    print("✅ COUNT MATCH - PASS")
else:
    print("❌ COUNT MISMATCH - FAIL")
    print(f"   Difference: {abs(source_count - target_count)} record(s)")


# =====================================================
# STEP 3 - NULL CHECK
# =====================================================
print("\n" + "=" * 50)
print("🔍 STEP 3 - NULL CHECK")
print("=" * 50)

source_nulls = source.isnull().sum()
target_nulls = target.isnull().sum()

print("Nulls in Source:")
print(source_nulls)
print("\nNulls in Target:")
print(target_nulls)

if source_nulls.sum() == 0:
    print("\n✅ NO NULLS IN SOURCE - PASS")
else:
    print("\n❌ NULLS FOUND IN SOURCE - FAIL")

if target_nulls.sum() == 0:
    print("✅ NO NULLS IN TARGET - PASS")
else:
    print("❌ NULLS FOUND IN TARGET - FAIL")


# =====================================================
# STEP 4 - DUPLICATE CHECK
# =====================================================
print("\n" + "=" * 50)
print("👯 STEP 4 - DUPLICATE CHECK")
print("=" * 50)

source_dups = source.duplicated().sum()
target_dups = target.duplicated().sum()

print(f"Duplicates in Source : {source_dups}")
print(f"Duplicates in Target : {target_dups}")

if source_dups == 0:
    print("✅ NO DUPLICATES IN SOURCE - PASS")
else:
    print("❌ DUPLICATES FOUND IN SOURCE - FAIL")
    print(source[source.duplicated()])

if target_dups == 0:
    print("✅ NO DUPLICATES IN TARGET - PASS")
else:
    print("❌ DUPLICATES FOUND IN TARGET - FAIL")
    print("\nDuplicate Rows:")
    print(target[target.duplicated()].to_string(index=False))


# =====================================================
# STEP 5 - COLUMN CHECK
# =====================================================
print("\n" + "=" * 50)
print("🔄 STEP 5 - COLUMN CHECK")
print("=" * 50)

source_cols = list(source.columns)
target_cols = list(target.columns)

print("Source Columns:", source_cols)
print("Target Columns:", target_cols)

if source_cols == target_cols:
    print("✅ COLUMNS MATCH - PASS")
else:
    print("❌ COLUMN MISMATCH - FAIL")


# =====================================================
# STEP 6 - MISSING RECORDS CHECK
# =====================================================
print("\n" + "=" * 50)
print("🔁 STEP 6 - MISSING RECORDS CHECK")
print("=" * 50)

source_ids = set(source["customer_id"])
target_ids = set(target["customer_id"])

missing_in_target = source_ids - target_ids
extra_in_target   = target_ids - source_ids

if len(missing_in_target) == 0:
    print("✅ NO MISSING RECORDS IN TARGET - PASS")
else:
    print("❌ MISSING RECORDS IN TARGET - FAIL")
    print("Missing Customer IDs:", missing_in_target)

if len(extra_in_target) == 0:
    print("✅ NO EXTRA RECORDS IN TARGET - PASS")
else:
    print("❌ EXTRA RECORDS IN TARGET - FAIL")
    print("Extra Customer IDs:", extra_in_target)


# =====================================================
# STEP 7 - FINAL VALIDATION REPORT
# =====================================================
print("\n" + "=" * 50)
print("       📊 FINAL VALIDATION REPORT")
print("=" * 50)
print(f"{'Tester':<25}: Namrata")
print(f"{'Source Records':<25}: {source_count}")
print(f"{'Target Records':<25}: {target_count}")
print("-" * 50)
print(f"{'STEP 2 - Count Check':<25}:",
      "✅ PASS" if source_count == target_count else "❌ FAIL")
print(f"{'STEP 3 - Null Check':<25}:",
      "✅ PASS" if source_nulls.sum() == 0 and target_nulls.sum() == 0 else "❌ FAIL")
print(f"{'STEP 4 - Duplicate Check':<25}:",
      "✅ PASS" if source_dups == 0 and target_dups == 0 else "❌ FAIL")
print(f"{'STEP 5 - Column Check':<25}:",
      "✅ PASS" if source_cols == target_cols else "❌ FAIL")
print(f"{'STEP 6 - Missing Records':<25}:",
      "✅ PASS" if len(missing_in_target) == 0 else "❌ FAIL")
print("=" * 50)
print("\n✅ Validation Complete!")
