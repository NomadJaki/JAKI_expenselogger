import tkinter as tk
from tkinter import ttk, messagebox

from expense_manager import add_expense, delete_expense, get_all_expenses
from report import calculate_total, category_summary
from search import search_expenses
from sorting import sort_by_amount
from visualization import show_pie_chart


window = tk.Tk()
window.title("Expense Logger")
window.geometry("1050x650")
window.resizable(False, False)


date_var = tk.StringVar()
category_var = tk.StringVar()
amount_var = tk.StringVar()
note_var = tk.StringVar()
search_var = tk.StringVar()


def clear_inputs():
    date_var.set("")
    category_var.set("")
    amount_var.set("")
    note_var.set("")


def refresh_table(expenses=None):
    if expenses is None:
        expenses = get_all_expenses()

    table.delete(*table.get_children())

    for expense in expenses:
        table.insert(
            "",
            tk.END,
            values=(
                expense.get("id", "N/A"),
                expense["date"],
                expense["category"],
                f"{float(expense['amount']):.2f}",
                expense["note"],
            ),
        )


def add_button_clicked():
    date = date_var.get().strip()
    category = category_var.get().strip()
    amount = amount_var.get().strip()
    note = note_var.get().strip()

    if date == "":
        messagebox.showerror("Error", "Please enter a date.")
        return

    if category == "":
        messagebox.showerror("Error", "Please enter a category.")
        return

    if amount == "":
        messagebox.showerror("Error", "Please enter an amount.")
        return

    try:
        amount_value = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")
        return

    add_expense(date, category, amount_value, note)
    clear_inputs()
    refresh_table()


def delete_button_clicked():
    selected_items = table.selection()
    if not selected_items:
        messagebox.showinfo("Delete", "Select a row to delete.")
        return

    selected_record = table.item(selected_items[0], "values")
    expense_id = selected_record[0]  # ID is the first column
    expense_info = f"{selected_record[1]} - {selected_record[2]}: ${selected_record[3]}"
    
    confirmed = messagebox.askyesno("Confirm delete", f"Delete this expense?\n{expense_info}")

    if confirmed:
        delete_expense(expense_id)
        refresh_table()
        messagebox.showinfo("Delete", "Expense deleted successfully.")


def sort_button_clicked():
    expenses = get_all_expenses()
    if not expenses:
        messagebox.showinfo("Sort", "No expenses to sort yet.")
        return

    sorted_expenses = sort_by_amount(expenses)
    refresh_table(sorted_expenses)
    messagebox.showinfo("Sort", "Expenses sorted by amount.")


def search_button_clicked():
    keyword = search_var.get().strip()
    if keyword == "":
        refresh_table()
        return

    results = search_expenses(get_all_expenses(), keyword)
    refresh_table(results)


def total_button_clicked():
    expenses = get_all_expenses()
    if not expenses:
        messagebox.showinfo("Overall Report", "No expenses recorded yet.")
        return

    total = calculate_total(expenses)
    summary = category_summary(expenses)
    summary_text = "\n".join(f"{name}: ${amount:.2f}" for name, amount in summary.items())
    messagebox.showinfo(
        "Overall Report",
        f"Number of records: {len(expenses)}\nTotal spending: ${total:.2f}\n\nCategory summary:\n{summary_text}",
    )


def chart_button_clicked():
    expenses = get_all_expenses()
    if not expenses:
        messagebox.showinfo("Chart", "No expenses available to plot.")
        return

    show_pie_chart(expenses)


input_frame = ttk.LabelFrame(window, text="Expense Details")
input_frame.pack(fill="x", padx=20, pady=10)

fields = [
    ("Date", date_var),
    ("Category", category_var),
    ("Amount", amount_var),
    ("Note", note_var),
]

for index, (label_text, variable) in enumerate(fields):
    ttk.Label(input_frame, text=label_text).grid(row=0, column=index * 2, padx=(10, 5), pady=8)
    ttk.Entry(input_frame, textvariable=variable, width=20).grid(row=0, column=index * 2 + 1, padx=(0, 10), pady=8)

button_frame = ttk.Frame(window)
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Add Expense", command=add_button_clicked).grid(row=0, column=0, padx=5)
ttk.Button(button_frame, text="Delete Expense", command=delete_button_clicked).grid(row=0, column=1, padx=5)
#ttk.Button(button_frame, text="Sort", command=sort_button_clicked).grid(row=0, column=2, padx=5)
ttk.Button(button_frame, text="Search", command=search_button_clicked).grid(row=0, column=3, padx=5)
ttk.Button(button_frame, text="Overall Report", command=total_button_clicked).grid(row=0, column=4, padx=5)
ttk.Button(button_frame, text="Show Chart", command=chart_button_clicked).grid(row=0, column=5, padx=5)

search_frame = ttk.Frame(window)
search_frame.pack(pady=5)
ttk.Label(search_frame, text="Search").grid(row=0, column=0, padx=5)
ttk.Entry(search_frame, textvariable=search_var, width=40).grid(row=0, column=1, padx=5)
ttk.Button(search_frame, text="Find", command=search_button_clicked).grid(row=0, column=2, padx=5)

columns = ("ID", "Date", "Category", "Amount", "Note")
table = ttk.Treeview(window, columns=columns, show="headings", height=15)
for col in columns:
    table.heading(col, text=col)
    if col == "ID":
        table.column(col, width=80)
    elif col == "Amount":
        table.column(col, width=100)
    else:
        table.column(col, width=150)
table.pack(pady=10)

refresh_table()
window.mainloop()
