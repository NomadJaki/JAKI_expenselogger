"""
validation.py

This module provides data validation for expenses.
Ensures data integrity and consistency.
"""

import re
from datetime import datetime


# Valid expense categories
VALID_CATEGORIES = {
    "Food",
    "Transport",
    "Entertainment",
    "Utilities",
    "Shopping",
    "Healthcare",
    "Education",
    "Housing",
    "Other"
}


def validate_date(date_str):
    """
    Validate date format (YYYY-MM-DD).
    
    Parameters:
        date_str (str): Date to validate
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not date_str or not date_str.strip():
        return False, "Date cannot be empty."
    
    date_str = date_str.strip()
    
    # Check format YYYY-MM-DD
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
        return False, "Date must be in YYYY-MM-DD format."
    
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True, ""
    except ValueError:
        return False, "Invalid date (e.g., 02-30 doesn't exist)."


def validate_category(category_str):
    """
    Validate category against predefined list.
    
    Parameters:
        category_str (str): Category to validate
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not category_str or not category_str.strip():
        return False, "Category cannot be empty."
    
    category_str = category_str.strip()
    
    if category_str not in VALID_CATEGORIES:
        valid_list = ", ".join(sorted(VALID_CATEGORIES))
        return False, f"Category must be one of: {valid_list}"
    
    return True, ""


def validate_amount(amount_str):
    """
    Validate amount is a positive number.
    
    Parameters:
        amount_str (str): Amount to validate
        
    Returns:
        tuple: (is_valid, error_message, amount_value)
    """
    if not amount_str or not amount_str.strip():
        return False, "Amount cannot be empty.", None
    
    amount_str = amount_str.strip()
    
    try:
        amount = float(amount_str)
    except ValueError:
        return False, "Amount must be a valid number.", None
    
    if amount <= 0:
        return False, "Amount must be greater than 0.", None
    
    if amount > 1000000:
        return False, "Amount cannot exceed $1,000,000.", None
    
    return True, "", amount


def validate_note(note_str):
    """
    Validate note (optional, but max length 500 chars).
    
    Parameters:
        note_str (str): Note to validate
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not note_str:
        return True, ""
    
    if len(note_str) > 500:
        return False, "Note cannot exceed 500 characters."
    
    return True, ""


def validate_expense(date, category, amount, note=""):
    """
    Validate all expense fields.
    
    Parameters:
        date (str): Expense date
        category (str): Expense category
        amount (str): Expense amount
        note (str): Expense note (optional)
        
    Returns:
        tuple: (is_valid, error_message, validated_amount)
    """
    # Validate date
    valid_date, date_msg = validate_date(date)
    if not valid_date:
        return False, date_msg, None
    
    # Validate category
    valid_cat, cat_msg = validate_category(category)
    if not valid_cat:
        return False, cat_msg, None
    
    # Validate amount
    valid_amt, amt_msg, amount_value = validate_amount(amount)
    if not valid_amt:
        return False, amt_msg, None
    
    # Validate note
    valid_note, note_msg = validate_note(note)
    if not valid_note:
        return False, note_msg, None
    
    return True, "", amount_value


def get_valid_categories():
    """Return list of valid categories."""
    return sorted(VALID_CATEGORIES)
