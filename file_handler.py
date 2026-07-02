import os
import json
from datetime import datetime

FILE_NAME = "expenses.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_data(expenses):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=4)

def backup_data():
    print("\n--- 10. Backup Data ---")
    if os.path.exists(FILE_NAME):
        backup_name = f"backup_expenses_{datetime.today().strftime('%Y%m%d')}.json"
        with open(FILE_NAME, "r", encoding="utf-8") as src, open(backup_name, "w", encoding="utf-8") as dst:
            dst.write(src.read())
        print(f"✅ Backup created successfully as '{backup_name}'!")
    else:
        print("❌ No data file found to backup.")