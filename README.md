# Expense Tracker

A simple, menu-driven expense tracker built with Python. It lets you add expenses, view the expenses you've entered, and calculate the total amount spent.

## Features

- **Add Expense** — enter an expense name and its cost.
- **View Expenses** — display all recorded expenses.
- **Show Total** — calculate and print the total cost of all recorded expenses.
- **Menu-driven interface** — choose an action from the command-line menu.

## How It Works

The project uses a **list of dictionaries** to store expense data:

- The list (`lis1`) holds all expenses.
- Each dictionary represents one expense and contains:
  - `item` — the name or description of the expense.
  - `amount` — the cost of the expense.

For example, an expense is stored in this format:

```python
{"item": "Notebook", "amount": 50}
```

The program has three main functions:

| Function | Purpose |
|---|---|
| `add_exp()` | Gets an expense name and cost from the user, then adds it to the list. |
| `display()` | Prints the stored expenses in a readable format using `pprint`. |
| `total()` | Adds the `amount` values of all expenses and prints the total. |

## Requirements

- Python 3

The project uses Python's built-in `pprint` module, so no additional packages are required.

## How to Run

1. Make sure Python 3 is installed.
2. Save the program as `exp_tracker.py`.
3. Open a terminal in the folder containing the file.
4. Run:

   ```bash
   python exp_tracker.py
   ```

   Depending on your setup, you may need to use `python3 exp_tracker.py` instead.

## Menu Options

When the program runs, choose an option:

1. **Add Expense** — enter the expense and its cost.
2. **View Expenses** — see the expenses entered during the current run.
3. **Show Total** — see the sum of all recorded expenses.
4. **Exit** — close the program.

## Current Limitations

- Expenses are stored in memory, so they are cleared when the program exits.
- Expense costs are entered as whole numbers.
- The program does not currently include editing, deleting, or saving expenses to a file.

## What I Practised

- Python lists and dictionaries
- Writing and calling functions
- Loops and conditional statements
- Getting input from users
- Iterating through a list to calculate a total
- Printing structured data with `pprint`

---

*This is a beginner Python project built to practise core programming concepts through a practical example.*
