"""
report.py

Generate reports from expense data.
"""



# Calculate total expense
def calculate_total(expenses):

    total = 0

    for expense in expenses:

        total += float(expense["amount"])

    return total



# Weekly report
def weekly_report(expenses):

    total = calculate_total(expenses)

    print("\nWeekly Report")
    print("---------------------")
    print(f"Number of records: {len(expenses)}")
    print(f"Total spending: ${total:.2f}")



# Category summary
def category_summary(expenses):

    summary = {}

    for expense in expenses:

        category = expense["category"]

        if category not in summary:

            summary[category] = 0

        summary[category] += float(expense["amount"])

    return summary

