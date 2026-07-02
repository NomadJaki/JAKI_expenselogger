from datetime import datetime
import file_handler

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

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
        print("❌ Invalid input! Amount must be a number, and date must be YYYY-MM-DD.")
        return

    expenses.append({"category": category, "amount": amount, "date": date_str})
    file_handler.save_data(expenses)
    print("✅ Expense added successfully!")

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
    elif choice == "2":
        expenses.sort(key=lambda x: x['amount'], reverse=True)
    else:
        print("❌ Invalid choice.")
        return
    file_handler.save_data(expenses)
    view_all_expenses(expenses)

# 5. Edit Expense
def edit_expense(expenses):
    print("\n--- 5. Edit Expense ---")
    view_all_expenses(expenses)
    if not expenses: return
    try:
        idx = int(input("Enter the ID of the expense to edit: "))
        if 0 <= idx < len(expenses):
            cat = input("Enter new category (press Enter to keep current): ").strip()
            amt = input("Enter new amount (press Enter to keep current): ").strip()
            dt = input("Enter new date (YYYY-MM-DD, press Enter to keep current): ").strip()
            
            if cat: expenses[idx]['category'] = cat
            if amt: expenses[idx]['amount'] = float(amt)
            if dt: 
                datetime.strptime(dt, '%Y-%m-%d')
                expenses[idx]['date'] = dt
                
            file_handler.save_data(expenses)
            print("✅ Expense updated successfully!")
        else:
            print("❌ Invalid ID.")
    except ValueError:
        print("❌ Invalid input.")

# 6. Delete Expense
def delete_expense(expenses):
    print("\n--- 6. Delete Expense ---")
    view_all_expenses(expenses)
    if not expenses: return
    try:
        idx = int(input("Enter the ID of the expense to delete: "))
        if 0 <= idx < len(expenses):
            removed = expenses.pop(idx)
            file_handler.save_data(expenses)
            print(f"✅ Deleted: {removed}")
        else:
            print("❌ Invalid ID.")
    except ValueError:
        print("❌ Invalid input.")

# 报告基础生成器
def _generate_report(expenses, period_name, filter_func):
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

# 7. Weekly Report
def weekly_report(expenses):
    current_week = datetime.today().isocalendar()[1]
    current_year = datetime.today().year
    filter_func = lambda d: datetime.strptime(d, '%Y-%m-%d').isocalendar()[1] == current_week and datetime.strptime(d, '%Y-%m-%d').year == current_year
    _generate_report(expenses, "Weekly", filter_func)

# 8. Monthly Report
def monthly_report(expenses):
    current_month = datetime.today().strftime('%Y-%m')
    filter_func = lambda d: d.startswith(current_month)
    _generate_report(expenses, "Monthly", filter_func)

# 9. Spending Charts
def spending_charts(expenses):
    print("\n--- 9. Spending Charts ---")
    if not plt:
        print("❌ matplotlib library is not installed. Run 'pip install matplotlib' to use this feature.")
        return
    if not expenses:
        print("No data to plot.")
        return
        
    summary = {}
    for e in expenses:
        summary[e['category']] = summary.get(e['category'], 0) + e['amount']
        
    plt.figure(figsize=(6, 6))
    plt.pie(list(summary.values()), labels=list(summary.keys()), autopct='%1.1f%%', startangle=140)
    plt.title("Expenses by Category")
    print("📊 Opening chart window...")
    plt.show()