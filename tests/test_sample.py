from financetracker.main import summarize


def test_summarize_no_args():
    assert summarize([]) == "FinanceTracker ready. No args provided."


def test_summarize_with_args():
    assert summarize(["a", "b"]) == "FinanceTracker called with: a, b"
