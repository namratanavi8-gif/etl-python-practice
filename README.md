# 🚀 ETL Data Validation Project

## 👩‍💻 About
Python script to validate Source vs Target data
- **Built by:** Namrata Navi
- **Role:** ETL Tester at Wipro | 3+ Years
- **Domain:** Retail(Costco, Home Depot)

## ✅ Validations Performed
| Check | Result |
|---|---|
| Count Check | ❌ FAIL — 1 record missing |
| Null Check | ✅ PASS — No nulls |
| Duplicate Check | ❌ FAIL — C001 duplicate |
| Column Check | ✅ PASS — All match |
| Missing Records | ❌ FAIL — C009, C010 missing |

## 🛠️ Tools Used
- Python 3.x
- Pandas
- Git & GitHub
- VS Code

## 📁 Files
| File | Description |
|---|---|
| etl_complete_validation.py | Main validation script |
| source_data.csv | Source data — 17 records |
| target_data.csv | Target data — has errors |

## ▶️ How to Run
### 1. Clone project
git clone https://github.com/namratanavi8-gif/etl-python-practice.git
### 2. Install pandas
pip install pandas
### 3. Run script
python etl_complete_validation.py

## 📊 Output
Source Records  : 17
Target Records  : 16
Count Check     : ❌ FAIL
Null Check      : ✅ PASS
Duplicate Check : ❌ FAIL
Column Check    : ✅ PASS
Missing Records : ❌ FAIL
