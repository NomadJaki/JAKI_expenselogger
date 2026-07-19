import unittest

from search import search_expenses


class ExpenseLoggerTests(unittest.TestCase):
    def test_search_expenses_finds_matching_category(self):
        expenses = [
            {"date": "2026-07-01", "category": "Food", "amount": 12.5, "note": "Lunch"},
            {"date": "2026-07-02", "category": "Travel", "amount": 8.0, "note": "Bus"},
        ]

        results = search_expenses(expenses, "food")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["category"], "Food")


if __name__ == "__main__":
    unittest.main()
