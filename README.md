# Expense Logger

## Student Information

**Name:** Jiaqi Sun

**ID Number:** 303065798 

**Course Code:** IY499 – Introduction to Programming

---

## Declaration

I confirm that this assignment is my own work.

Where I have referred to online sources, I have provided comments detailing the reference and included a link to the original source where appropriate.

---

## Project Description

Expense Logger is a Python desktop application developed to record and manage daily expenses. Users can add, edit, delete, search and sort expense records through a simple graphical user interface. All expense data is stored locally in a JSON file, allowing users to save and retrieve their records between sessions.

The application also generates weekly spending reports and provides charts to help users analyse their spending habits. During development, the project demonstrates the programming concepts covered in the module, including variables, data types, arithmetic operations, selection, iteration, functions, file input and output, recursion, searching algorithms, sorting algorithms, data visualisation, error handling and user interface design.

---

## Libraries Used

This project uses the following Python libraries:

- tkinter
- json
- datetime
- uuid
- os
- matplotlib
- unittest

Additional libraries (if required) are listed in `requirements.txt`.

---

## Installation

1. Install Python 3.10 or above.
2. Download or clone this project.
3. Open a terminal in the project folder.
4. Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Program

Run the application with:

```bash
python main.py
```

The program will automatically create an `expenses.json` file if one does not already exist.

---

## Project Structure

```text
ExpenseLogger/
│
├── main.py
├── expense_manager.py
├── file_handler.py
├── report.py
├── search.py
├── sorting.py
├── validation.py
├── visualization.py
├── expenses.json
├── requirements.txt
├── test_expense_logger.py
└── README.md
```

---

## Features

- Add new expense records
- Edit existing expenses
- Delete expenses
- Search expenses by keyword or category
- Sort expenses by amount or date
- Generate weekly spending reports
- Display spending charts
- Save and load data using JSON
- Input validation and error handling

---

## Git Repository

Repository:

```
https://github.com/your-username/ExpenseLogger
```