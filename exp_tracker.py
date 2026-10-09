import pprint
lis1 = []


while True:
    def add_exp():
            item = input("expenses")
            cost = int(input("cost"))
            exp = {}
            exp["item"] = item
            exp["amount"] = cost
            lis1.append(exp)
    
    def display():
            pprint.pprint(lis1)
    
    def total():
        totals = 0
        for i in range(len(lis1)):
            totals += lis1[i]["amount"]
        print(totals)
    
    
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_exp()
        

    elif choice == "2":
        display()
        

    elif choice == "3":
        total()

    elif choice == "4":
        break





