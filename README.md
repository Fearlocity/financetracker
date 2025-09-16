# financetracker

Minimal Python project scaffold for FinanceTracker.

Setup (Windows PowerShell):

Open PowerShell in the project root (where this README lives) and run:

```powershell
# create the virtual environment
python -m venv .venv

# activate the venv for the current PowerShell session
.\.venv\Scripts\Activate.ps1

# upgrade pip/setuptools and install project deps
python -m pip install -U pip setuptools
pip install -r requirements.txt
```

Run tests:

```powershell
# ensure PYTHONPATH contains the src dir so the package is importable
$env:PYTHONPATH = "$PWD\\src"
pytest -q
```

Or run the module directly (example - will prompt for input):

```powershell
$env:PYTHONPATH = "$PWD\\src"
python .\src\financetracker\main.py
```

```