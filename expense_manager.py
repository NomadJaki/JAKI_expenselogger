"""
expense_manager.py

This module manages expense records.
It provides functions to add, update, delete,
and retrieve expenses.
Each expense has a unique ID for reliable identification.
"""

from file_handler import load_expenses, save_expenses
import uuid


def generate_expense_id():
    """Generate a unique ID for an expense."""
    return str(uuid.uuid4())[:8]  # Use first 8 characters of UUID


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
        "id": generate_expense_id(),
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    }

    expenses.append(new_expense)

    save_expenses(expenses)
    return new_expense["id"]


# Return all expense records
def get_all_expenses():
    """
    Return every expense stored in the JSON file.
    """

    return load_expenses()


# Delete an expense by ID
def delete_expense(expense_id):
    """
    Delete an expense record by its unique ID.

    Parameters:
        expense_id (str): The unique ID of the expense to delete
    """

    expenses = load_expenses()

    new_list = [exp for exp in expenses if exp.get("id") != expense_id]

    save_expenses(new_list)


# Delete an expense by matching fields (legacy support)
def delete_expense_by_record(selected_record):
    """
    Delete an expense record by matching all fields.
    DEPRECATED: Use delete_expense(expense_id) instead.

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
def update_expense(expense_id,
                   new_date,
                   new_category,
                   new_amount,
                   new_note):
    """
    Update an expense record by its unique ID.
    
    Parameters:
        expense_id (str): The unique ID of the expense to update
        new_date (str): New date value
        new_category (str): New category value
        new_amount (float): New amount value
        new_note (str): New note value
    """

    expenses = load_expenses()

    for expense in expenses:

        if expense.get("id") == expense_id:

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
