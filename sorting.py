"""
sorting.py

This module sorts expense records.
"""



# Bubble Sort by Amount
def sort_by_amount(expenses):

    sorted_list = expenses.copy()

    n = len(sorted_list)

    for i in range(n):

        for j in range(0, n - i - 1):

            if sorted_list[j]["amount"] > sorted_list[j + 1]["amount"]:

                sorted_list[j], sorted_list[j + 1] = \
                    sorted_list[j + 1], sorted_list[j]

    return sorted_list



# Bubble Sort by Date
def sort_by_date(expenses):

    sorted_list = expenses.copy()

    n = len(sorted_list)

    for i in range(n):

        for j in range(0, n - i - 1):

            if sorted_list[j]["date"] > sorted_list[j + 1]["date"]:

                sorted_list[j], sorted_list[j + 1] = \
                    sorted_list[j + 1], sorted_list[j]

    return sorted_list