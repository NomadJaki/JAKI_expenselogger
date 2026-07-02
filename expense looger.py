import os

FILE_NAME = "expenses.txt"

def load_expenses():
    expenses = []
    if not os.path.exists(FILE_NAME):
        return expenses

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                category, amount = line.split(",")
                expenses.append({
                    "category": category,
                    "amount": float(amount)
                })
    return expenses

def save_expense(category, amount):
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(f"{category},{amount}\n")

def log_expense(expenses):
    print("\n--- Record new expense ---")
    category = input("Please enter the expense category (e.g., Food, Transportation, Entertainment): ").strip()

    try:
        amount = float(input("Please enter the expense amount: "))
        if amount < 0:
            print("Amount cannot be negative!")
            return
    except ValueError:
        print("Input is invalid, please enter a number!")
        return

    save_expense(category, amount)
    expenses.append({"category": category, "amount": amount})
    print(f"Success: [{category}] spent ￥{amount:.2f}")

def show_summary(expenses):
    print("\n--- Expense Summary Report ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    summary = {}
    total_spend = 0.0

    for item in expenses:
        category = item["category"]
        amount = item["amount"]
        
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
        
        total_spend += amount

    # 打印分类统计结果
    print(f"{'Category':<10}{'Total Amount':<10}")
    print("-" * 25)
    for category, amount in summary.items():
        print(f"{category:<10}￥{amount:<10.2f}")
    
    print("-" * 25)
    print(f"Total Expenses: ￥{total_spend:.2f}\n")

def main():
    """main loop for the expense tracker program"""
    expenses = load_expenses()
    
    while True:
        print("=== Expense Tracker ===")
        print("1. Record new expense")
        print("2. View expense report")
        print("3. Exit program")
        
        choice = input("Please select an option (1-3): ").strip()
        
        if choice == "1":
            log_expense(expenses)
        elif choice == "2":
            show_summary(expenses)
        elif choice == "3":
            print("Thank you for using the expense tracker, goodbye!")
            break
        else:
            print("Invalid option, please try again.\n")

# 运行主程序
if __name__ == "__main__":
    main()