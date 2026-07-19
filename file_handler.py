"""
file_handler.py

This module handles all file operations.
It loads expense data from a JSON file,
saves data back to the file,
and creates backup files.
"""

import json
import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "expenses.json")


def load_expenses():
    """Load expense records from the JSON file."""

    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        print("Error: JSON file is corrupted.")
        return []
    except Exception as e:
        print("Unexpected error:", e)
        return []


def save_expenses(expenses):
    """Save all expenses into the JSON file."""

    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)
    except Exception as e:
        print("Error saving file:", e)


def backup_data():
    """Create a backup of expenses.json."""

    backup_name = os.path.join(BASE_DIR, "expenses_backup.json")

    try:
        shutil.copy(FILE_NAME, backup_name)
        print("Backup created successfully.")
    except FileNotFoundError:
        print("No expense file found.")
    except Exception as e:
        print("Backup failed:", e)


def clear_data():
    """Delete all expense records."""

    save_expenses([])


def file_exists():
    """Returns True if expenses.json exists."""

    return os.path.exists(FILE_NAME)