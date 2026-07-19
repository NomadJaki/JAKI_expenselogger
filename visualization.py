"""
visualization.py

This module provides lightweight visualization helpers
without depending on matplotlib. It shows simple text
summaries (used by the Tkinter UI) so the project has
no external plotting dependency.
"""

from report import category_summary
from tkinter import messagebox


def show_pie_chart(expenses):
    """Show a text-based category breakdown via messagebox."""
    summary = category_summary(expenses)
    total = sum(summary.values())

    if total == 0:
        messagebox.showinfo("Chart", "No expenses to summarize.")
        return

    lines = []
    for cat, amt in summary.items():
        pct = (amt / total) * 100
        lines.append(f"{cat}: ${amt:.2f} ({pct:.1f}%)")

    message = "Category breakdown:\n\n" + "\n".join(lines)
    messagebox.showinfo("Expense Summary", message)


def show_bar_chart(expenses):
    """Show a simple ASCII bar summary in a messagebox."""
    summary = category_summary(expenses)
    if not summary:
        messagebox.showinfo("Chart", "No expenses to summarize.")
        return

    max_label_len = max(len(k) for k in summary.keys())
    max_amount = max(summary.values())
    scale = 40 / max_amount if max_amount > 0 else 1

    lines = []
    for cat, amt in summary.items():
        bar = "#" * int(amt * scale)
        lines.append(f"{cat.rjust(max_label_len)} | {bar} {amt:.2f}")

    message = "Expense bar chart:\n\n" + "\n".join(lines)
    messagebox.showinfo("Expense Chart", message)
