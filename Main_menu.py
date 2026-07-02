import os
import json
from datetime import datetime


try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

FILE_NAME = "expenses_v2.json"

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

# 1. Add Expense
def add_expense(expenses):
    print("\n--- 1. Add Expense ---")
    category = input("Enter category (e.g., Food, Transport): ").strip()
    try:
        amount = float(input("Enter amount: "))
        date_str = input("Enter date (YYYY-MM-DD, press Enter for Today): ").strip()
        if not date_str:
            date_str = datetime.today().strftime('%Y-%m-%d')
        else:
            datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print("Invalid input! Amount must be a number, and date must be YYYY-MM-DD.")
        return

    expense = {"category": category, "amount": amount, "date": date_str}
    expenses.append(expense)
    save_data(expenses)
    print("Expense added successfully!")

# 2. View All Expenses
def view_all_expenses(expenses):
    print("\n--- 2. View All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return
    print(f"{'ID':<5}{'Date':<15}{'Category':<15}{'Amount':<10}")
    print("-" * 45)
    for i, exp in enumerate(expenses):
        print(f"{i:<5}{exp['date']:<15}{exp['category']:<15}${exp['amount']:<10.2f}")

# 3. Search Expenses
def search_expenses(expenses):
    print("\n--- 3. Search Expenses ---")
    keyword = input("Enter keyword to search (category or date): ").strip().lower()
    results = [e for e in expenses if keyword in e['category'].lower() or keyword in e['date']]
    
    if not results:
        print("No matching expenses found.")
    else:
        view_all_expenses(results)

# 4. Sort Expenses
def sort_expenses(expenses):
    print("\n--- 4. Sort Expenses ---")
    print("1. Sort by Date (Newest First)")
    print("2. Sort by Amount (Highest First)")
    choice = input("Choose sorting option (1-2): ").strip()
    
    if choice == "1":
        expenses.sort(key=lambda x: x['date'], reverse=True)
        print("Sorted by date.")
    elif choice == "2":
        expenses.sort(key=lambda x: x['amount'], reverse=True)
        print("Sorted by amount.")
    else:
        print("Invalid choice.")
        return
    save_data(expenses)
    view_all_expenses(expenses)

# 5. Edit Expense
def edit_expense(expenses):
    print("\n--- 5. Edit Expense ---")
    view_all_expenses(expenses)
    if not expenses: return
    try:
        idx = int(input("Enter the ID of the expense to edit: "))
        if 0 <= idx < len(expenses):
            print(f"Current details: {expenses[idx]}")
            cat = input("Enter new category (press Enter to keep current): ").strip()
            amt = input("Enter new amount (press Enter to keep current): ").strip()
            dt = input("Enter new date (YYYY-MM-DD, press Enter to keep current): ").strip()
            
            if cat: expenses[idx]['category'] = cat
            if amt: expenses[idx]['amount'] = float(amt)
            if dt: 
                datetime.strptime(dt, '%Y-%m-%d')
                expenses[idx]['date'] = dt
                
            save_data(expenses)
            print("Expense updated successfully!")
        else:
            print("Invalid ID.")
    except ValueError:
        print("Invalid input.")

# 6. Delete Expense
def delete_expense(expenses):
    print("\n--- 6. Delete Expense ---")
    view_all_expenses(expenses)
    if not expenses: return
    try:
        idx = int(input("Enter the ID of the expense to delete: "))
        if 0 <= idx < len(expenses):
            removed = expenses.pop(idx)
            save_data(expenses)
            print(f"Deleted: {removed}")
        else:
            print("Invalid ID.")
    except ValueError:
        print("Invalid input.")


def generate_report(expenses, period_name, filter_func):
    print(f"\n--- {period_name} Report ---")
    filtered = [e for e in expenses if filter_func(e['date'])]
    if not filtered:
        print(f"No expenses found for this {period_name.lower()}.")
        return
    
    summary = {}
    total = 0
    for e in filtered:
        cat, amt = e['category'], e['amount']
        summary[cat] = summary.get(cat, 0) + amt
        total += amt
        
    for cat, amt in summary.items():
        print(f"- {cat}: ${amt:.2f}")
    print(f"Total Spending: ${total:.2f}")

# 7. Weekly Report (make samply by calculate weekly)
def weekly_report(expenses):
    current_week = datetime.today().isocalendar()[1]
    current_year = datetime.today().year
    filter_func = lambda d: datetime.strptime(d, '%Y-%m-%d').isocalendar()[1] == current_week and datetime.strptime(d, '%Y-%m-%d').year == current_year
    generate_report(expenses, "Weekly", filter_func)

# 8. Monthly Report
def monthly_report(expenses):
    current_month = datetime.today().strftime('%Y-%m')
    filter_func = lambda d: d.startswith(current_month)
    generate_report(expenses, "Monthly", filter_func)

# 9. Spending Charts
def spending_charts(expenses):
    print("\n--- 9. Spending Charts ---")
    if not plt:
        print("matplotlib library is not installed. Run 'pip install matplotlib' to use this feature.")
        return
    if not expenses:
        print("No data to plot.")
        return
        
    summary = {}
    for e in expenses:
        summary[e['category']] = summary.get(e['category'], 0) + e['amount']
        
    labels = list(summary.keys())
    sizes = list(summary.values())
    
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Expenses by Category")
    print("Opening chart window...")
    plt.show()

# 10. Backup Data
def backup_data():
    print("\n--- 10. Backup Data ---")
    if os.path.exists(FILE_NAME):
        backup_name = f"backup_expenses_{datetime.today().strftime('%Y%m%d')}.json"
        with open(FILE_NAME, "r", encoding="utf-8") as src, open(backup_name, "w", encoding="utf-8") as dst:
            dst.write(src.read())
        print(f"Backup created successfully as '{backup_name}'!")
    else:
        print("No data file found to backup.")

# main loop
def main():
    expenses = load_data()
    while True:
        print("\n========== Expense Logger ==========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expenses")
        print("4. Sort Expenses")
        print("5. Edit Expense")
        print("6. Delete Expense")
        print("7. Weekly Report")
        print("8. Monthly Report")
        print("9. Spending Charts")
        print("10. Backup Data")
        print("11. Exit")
        print("====================================")
        
        choice = input("Choose an option (1-11): ").strip()
        
        if choice == "1": add_expense(expenses)
        elif choice == "2": view_all_expenses(expenses)
        elif choice == "3": search_expenses(expenses)
        elif choice == "4": sort_expenses(expenses)
        elif choice == "5": edit_expense(expenses)
        elif choice == "6": delete_expense(expenses)
        elif choice == "7": weekly_report(expenses)
        elif choice == "8": monthly_report(expenses)
        elif choice == "9": spending_charts(expenses)
        elif choice == "10": backup_data()
        elif choice == "11":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid option. Please enter 1-11.")

if __name__ == "__main__":
    main()
