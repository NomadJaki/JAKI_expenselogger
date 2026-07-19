# Expense Logger

A simple desktop application to record and manage your money spending. You can add expenses, find them, and see reports about your spending habits.

## What Can You Do?

- **Add Expenses**: Write down what you spent money on with the date, type, amount, and notes
- **Delete Expenses**: Remove expenses you do not need anymore
- **Search**: Find expenses by typing keywords
- **Sort**: Arrange expenses by amount of money
- **Reports**: See how much money you spent and which category costs the most
- **Charts**: View pictures that show your spending by category
- **Save Data**: All expenses are saved in a file on your computer

## File Explanation

The project has these files:

- `main.py` - The program window and buttons (start here)
- `expense_manager.py` - Add, delete, and change expenses
- `file_handler.py` - Save and load expenses from a file
- `report.py` - Calculate totals and category information
- `search.py` - Find expenses with keywords
- `sorting.py` - Arrange expenses in different orders
- `validation.py` - Check if the information is correct
- `visualization.py` - Make charts and pictures
- `expenses.json` - Where all expenses are saved
- `requirements.txt` - List of extra software needed
- `test_expense_logger.py` - Tests to check the program works

## Requirements (What You Need)

- Python 3.x or higher
- No extra software packages needed (Python includes everything)

Optional:
- `matplotlib` - For better looking charts (not necessary)

## How to Start

**Step 1: Download or Copy**

Copy the project files to your computer.

**Step 2: Open the Folder**

Open your computer terminal or command prompt. Go to the folder:

```
cd JAKI_expenselogger
```

**Step 3: Run the Program**

Type this command:

```
python main.py
```

The program window will open. You can now use it.

**Step 4: Optional - Install Extra Software**

If you want better charts, you can install matplotlib:

```
pip install matplotlib
```

## How to Use

### Add a New Expense

1. Write the date in this format: `2024-01-15` (year-month-day)
2. Choose a category from the list (Food, Transport, Entertainment, etc.)
3. Enter the amount of money
4. Add a note if you want to remember what it was for
5. Click the "Add Expense" button
6. The expense will appear in the table below

### Remove an Expense

1. Click on the expense in the table
2. Click "Delete Expense"
3. A question will appear - click "Yes" to confirm
4. The expense is deleted

### Find an Expense

1. Type a word or date in the search box
2. Click "Find"
3. The table will show only the expenses that match
4. Click "Find" again with an empty search box to see all expenses

### Sort Expenses by Amount

1. Click "Sort by Amount"
2. Expenses will arrange from smallest to largest amount
3. You can see which costs you are spending the most on

### See a Report

1. Click "Overall Report"
2. A window will show:
   - How many expenses you have
   - Total amount of money spent
   - How much you spent in each category

### View a Chart

1. Click "Show Chart"
2. A table will appear showing:
   - Each category
   - How much money in each category
   - What percentage of your total spending

### Filter by Category

1. Click "Filter by Category"
2. Choose a category from the list
3. The table will show only expenses from that category

## Categories Available

These are the expense types you can choose:

- Food (eating and drinks)
- Transport (cars, buses, trains)
- Entertainment (movies, games, fun)
- Utilities (water, electricity, internet)
- Shopping (clothes, books, things)
- Healthcare (doctor, medicine, health)
- Education (classes, courses, books)
- Housing (rent, home, house)
- Other (anything else)

## How Data is Saved

Your expenses are saved in a file called `expenses.json`. This is a text file that stores information like this:

```
[
  {
    "id": "abc12345",
    "date": "2024-01-15",
    "category": "Food",
    "amount": 25.50,
    "note": "Lunch with colleagues"
  }
]
```

Each expense has:
- `id` - A unique number (so you can have two expenses exactly the same)
- `date` - When you spent the money
- `category` - What type of expense it is
- `amount` - How much money
- `note` - Extra information about the expense

## Rules for Adding Expenses

The program checks your information before saving:

1. **Date** - Must be in format `YYYY-MM-DD` (like `2024-01-15`). The date must be real (not like February 30).
2. **Category** - Must be from the list above. You cannot write your own category.
3. **Amount** - Must be a number. It must be more than 0 and less than 1,000,000.
4. **Note** - Can be empty or have words. Maximum 500 letters.

If something is wrong, the program will tell you the problem.

## Technical Information

- **Sorting** - Uses fast sorting (very quick even for many expenses)
- **Unique IDs** - Each expense has its own special number. You can have two expenses that are exactly the same
- **No Internet** - Everything works offline on your computer
- **Safe** - Data stays on your computer. No information goes online

## How to Test

If you want to check that the program works correctly:

```
python test_expense_logger.py
```

This will run tests to make sure all the parts work.

## Important Notes

- All data is on your computer only
- Make a backup copy of `expenses.json` if you want to be safe
- You can open `expenses.json` in any text editor to see your expenses
- Works on Windows, Mac, and Linux
- The program is simple and easy to use
- No special knowledge needed to use it
