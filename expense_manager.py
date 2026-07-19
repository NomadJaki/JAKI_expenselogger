"""
expense_manager.py

This module manages expense records.
It provides functions to add, update, delete,
and retrieve expenses.
"""

from file_handler import load_expenses, save_expenses



# Add a new expense
def add_expense(date, category, amount, note):
    """
    Add a new expense to the expense list.

    Parameters:
        date (str)
        category (str)
        amount (float)
        note (str)
    """

    expenses = load_expenses()

    new_expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    }

    expenses.append(new_expense)

    save_expenses(expenses)



# Return all expense records
def get_all_expenses():
    """
    Return every expense stored in the JSON file.
    """

    return load_expenses()



# Delete an expense
def delete_expense(selected_record):
    """
    Delete an expense record.

    selected_record should contain:
    (date, category, amount, note)
    """

    expenses = load_expenses()

    new_list = []

    for expense in expenses:

        if not (
            expense["date"] == selected_record[0]
            and expense["category"] == selected_record[1]
            and float(expense["amount"]) == float(selected_record[2])
            and expense["note"] == selected_record[3]
        ):

            new_list.append(expense)

    save_expenses(new_list)



# Update an existing expense
def update_expense(old_record,
                   new_date,
                   new_category,
                   new_amount,
                   new_note):
    """
    Update one expense record.
    """

    expenses = load_expenses()

    for expense in expenses:

        if (
            expense["date"] == old_record[0]
            and expense["category"] == old_record[1]
            and float(expense["amount"]) == float(old_record[2])
            and expense["note"] == old_record[3]
        ):

            expense["date"] = new_date
            expense["category"] = new_category
            expense["amount"] = new_amount
            expense["note"] = new_note

            break

    save_expenses(expenses)


# Count total number of expenses
def count_expenses():
    """
    Return the total number of expense records.
    """

    expenses = load_expenses()

    return len(expenses)


# Calculate total amount spent
def get_total_amount():
    """
    Return the total amount of all expenses.
    """

    expenses = load_expenses()

    total = 0

    for expense in expenses:

        total += float(expense["amount"])

    return total


# Get all expenses in a category
def get_category_expenses(category):
    """
    Return all expenses in the specified category.
    """

    expenses = load_expenses()

    results = []

    for expense in expenses:

        if expense["category"].lower() == category.lower():

            results.append(expense)

    return results
