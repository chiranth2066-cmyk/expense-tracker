# Expense Tracker

A simple, terminal-based expense tracker built with Python. Track daily spending, organize expenses by category, and manage your records using a local JSON file.

## Features

- **Add expenses** — Record the category, item name, and amount.
- **View expenses** — Display expenses organized by date.
- **Calculate total spending** — Find the total amount spent across all recorded dates.
- **Edit expenses** — Update the amount of an existing expense.
- **Delete expenses** — Remove expenses you no longer need.
- **Persistent storage** — Save your data locally in `store.json`.

## Tech Stack

- Python
- JSON for data storage
- `datetime` for date handling
- `pprint` for formatted output

## Project Structure

```text
expense-tracker/
├── main.py
├── store.json
└── README.md
```

*Note: Replace `main.py` with your actual Python filename if it differs.*

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/chiranth2066-cmyk/expense-tracker.git
cd expense-tracker
```

### 2. Run the application

```bash
python main.py
```

Make sure Python 3 is installed on your system.

### 3. Use the menu

```text
Expense Tracker
1. Add Expense
2. View Expenses
3. Show Total
4. Edit
5. Delete
```

Choose an option and follow the terminal prompts.

## Data Storage

Expenses are stored in `store.json`, grouped by date.

Example:

```json
{
  "2026-10-22": [
    {
      "category": "Food",
      "item": "Lunch",
      "amount": 150
    }
  ]
}
```

Your expense records are stored locally, so keep a backup of `store.json` if the data matters to you.

## Version History

### v2.0
- Added expense editing.
- Added expense deletion.
- Improved expense display and total calculation.
- Organized expense records by date.

## Future Improvements

- Filter expenses by category.
- Generate monthly expense summaries.
- Add input validation and error handling.
- Display spending trends and reports.
- Build a graphical user interface.

## Author

**Chiranth C**

[GitHub Repository](https://github.com/chiranth2066-cmyk/expense-tracker)

---

Built as a Python project to practice functions, dictionaries, lists, loops, file handling, and JSON data management.
