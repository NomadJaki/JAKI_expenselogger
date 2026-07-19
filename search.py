"""
search.py

This module provides search functions
for expense records.
"""


def search_expenses(expenses, keyword):
    """Search expenses by category, note, or date."""

    results = []
    keyword = keyword.lower().strip()

    if keyword == "":
        return list(expenses)

    for expense in expenses:
        if (
            keyword in expense["category"].lower()
            or keyword in expense["note"].lower()
            or keyword in expense["date"].lower()
        ):
            results.append(expense)

    return results


def search_by_category(expenses, keyword):
    """Search expenses by category."""

    results = []
    keyword = keyword.lower().strip()

    for expense in expenses:
        if keyword in expense["category"].lower():
            results.append(expense)

    return results


def search_by_note(expenses, keyword):
    """Search expenses by note."""

    results = []
    keyword = keyword.lower().strip()

    for expense in expenses:
        if keyword in expense["note"].lower():
            results.append(expense)

    return results


def search_by_date(expenses, date):
    """Search expenses by exact date."""

    results = []

    for expense in expenses:
        if expense["date"] == date:
            results.append(expense)

    return results
