"""Simple entry point for the FinanceTracker app."""

from typing import List


def summarize(args: List[str]) -> str:
    """Return a short message summarizing the provided args."""
    if not args:
        return "FinanceTracker ready. No args provided."
    return f"FinanceTracker called with: {', '.join(args)}"


def main(argv: List[str] | None = None) -> int:
    income = input("Enter your income: ")
    expenses = dict()
    while input("Add an expense? (y/n): ").lower() == 'y':
        expense_name = input("Expense name: ")
        expense_amount = input("Expense amount: ")
        expenses[expense_name] = expense_amount
    print(f"Income: {income}, Expenses: {expenses}")
    if argv is None:
        import sys

        argv = sys.argv[1:]
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
