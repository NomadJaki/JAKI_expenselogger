import file_handler
import expense_manager

def main():
    expenses = file_handler.load_data()
    
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
        
        if choice == "1": expense_manager.add_expense(expenses)
        elif choice == "2": expense_manager.view_all_expenses(expenses)
        elif choice == "3": expense_manager.search_expenses(expenses)
        elif choice == "4": expense_manager.sort_expenses(expenses)
        elif choice == "5": expense_manager.edit_expense(expenses)
        elif choice == "6": expense_manager.delete_expense(expenses)
        elif choice == "7": expense_manager.weekly_report(expenses)
        elif choice == "8": expense_manager.monthly_report(expenses)
        elif choice == "9": expense_manager.spending_charts(expenses)
        elif choice == "10": file_handler.backup_data()
        elif choice == "11":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid option. Please enter 1-11.")

if __name__ == "__main__":
    main()