import json
from datetime import date
with open("store.json", "r") as fila:
    lis1 = json.load(fila)







def add_exp():
        today = date.today().isoformat()
        catogory = input("catogory")
        item = input("item")
        cost = int(input("cost"))
        
        exp = {}
        exp["catogory"] = catogory
        exp["item"] = item
        exp["amount"] = cost
    
        if today not in lis1:
            lis1[today] = []

        lis1[today].append(exp)

        with open("store.json", "w") as file:
            json.dump(lis1, file, indent=4)


def display():
    for dat, expenses in lis1.items():
        print(f"\nDate: {dat}")
        for i, exp in enumerate(expenses, start=1):
            print(f"{i}. {exp}")

def total():
    totals = 0

    for expenses in lis1.values():
        for exp in expenses:
            totals += exp["amount"]

    print("Total expenses:", totals)

def edit():
    display()

    dat = input("Enter date (YYYY-MM-DD): ")

    if dat not in lis1:
        print("Date not found")
        return

    n = int(input("Enter expense number to edit: "))

    if 1 <= n <= len(lis1[dat]):
        new_val = int(input("Enter new amount: "))
        lis1[dat][n - 1]["amount"] = new_val

        with open("store.json", "w") as file:
            json.dump(lis1, file, indent=4)

        print("Expense updated successfully")
    else:
        print("Invalid expense number")

def delete():
    x = int(input("the expense u want to remove"))
    lis1.pop(x-1)
    
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Edit")
    print("5. delete")

    choice = input("Choose an option: ")

    if choice == "1":
        add_exp()
        

    elif choice == "2":
        display()
        

    elif choice == "3":
        total()

    elif choice == "4":
        edit()

    elif choice == "5":
         delete()
    else:
         break





