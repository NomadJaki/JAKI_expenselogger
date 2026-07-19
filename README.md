# Expense Logger
'''
I confirm that this assignment is my own work. Where I have referred to online sources, I have provided comments detailing the reference and included a link to the source.
'''
A desktop application for tracking and managing personal expenses with a graphical user interface built with Python's Tkinter library.

## Features

- **Add Expenses**: Record new expenses with date, category, amount, and notes
- **Delete Expenses**: Remove expense records from your history
- **Search Expenses**: Find expenses by date, category, or notes
- **Sort Expenses**: Sort expenses by amount
- **Category Summary**: View spending breakdown by category
- **Visualizations**: Generate pie charts to visualize expense distribution
- **Data Persistence**: All expenses are stored in JSON format for easy backup and portability

## Project Structure

'''
.
├── main.py                   # GUI application entry point (Tkinter)
├── expense_manager.py        # Core expense management functions
├── file_handler.py           # JSON file operations (load/save)
├── report.py                 # Reporting and analysis functions
├── search.py                 # Search and filter functionality
├── sorting.py                # Sorting operations
├── visualization.py          # Chart and visualization utilities
├── test_expense_logger.py    # Unit tests
├── expenses.json             # Data storage (auto-created)
├── requirements.txt          # Project dependencies
└── README.md                 # This file
'''

## Requirements

- Python 3.x
- No external dependencies (uses Python standard library only)
  - `tkinter` (included with Python)
  - `json` (standard library)
  - `matplotlib` (optional, for advanced visualizations)

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   '''bash
   cd JAKI_expenselogger
   '''
3. (Optional) Install any optional dependencies:
   '''bash
   pip install -r requirements.txt
   '''

## Usage

Run the application:
```bash
python main.py
'''

The GUI will open with the following features:

### Adding an Expense
1. Enter the date (e.g., 2024-01-15)
2. Select or enter a category (e.g., Food, Transport, Entertainment)
3. Enter the amount
4. Add an optional note
5. Click "Add Expense"

### Viewing Expenses
- All expenses are displayed in a table format
- View date, category, amount, and notes for each entry

### Searching
- Use the search bar to find expenses by keyword
- Search works across date, category, and notes fields

### Sorting & Analysis
- Sort expenses by amount to see highest or lowest spending
- View category summaries to understand spending patterns
- Generate visualization charts

### Deleting Expenses
1. Select an expense row from the table
2. Click "Delete"
3. Confirm the deletion

## Data Storage

Expenses are automatically saved to `expenses.json` in the following format:
'''json
[
  {
    "date": "2024-01-15",
    "category": "Food",
    "amount": 25.50,
    "note": "Lunch with colleagues"
  }
]
'''

## Testing

Run the test suite:
'''bash
python test_expense_logger.py
'''

## Notes

- All data is stored locally in JSON format
- No internet connection required
- Works on Windows, macOS, and Linux
- Simple and lightweight interface
