#January 14, 2026

#Final Project for Python Foundations. 
# Personal Expense Tracker (CLI)

def get_user_choice():
    while True:
        print("Services: \n")
        print("1. Add Expense.")
        print("2. View Expense.")
        print("3. Calculation of expense.")
        print("4. Exit")
        
        user_input = input("\nEnter: ")
        
        try:
            user_input = int(user_input)
        except ValueError:
            print("Invalid Input.")
        else:
            if user_input < 1 or user_input > 4:
                print("Please choose from 1 - 4.")
            else:
                return user_input
        
def add_expense(data):
    data_list = []
    while True:
        category = get_category().upper()
        amount = get_amount()
        
        if duplication_check(category, data):
            print("Category is already made, will only add the amount given.")
            data_list = data[f"{category}"]
            data_list.append(amount)
            data.update({f"{category}" : data_list})
            break
        else:
            data_list.append(amount)
            data.update({f"{category}" : data_list})
            break

def get_category():
    while True: 
        category = input("Type of Expense: ")
        
        if len(category) == 0:
            print("Category name can't be blank.")
        else:
            return category
        
def get_amount():
    while True: 
        amount = input("Amount: ")
        
        try: 
            amount = int(amount)
        except ValueError:
            print("Invalid Input.")
        else:
            if amount <= 0:
                print("Amount can't be lower or equal to 0.")
            else: 
                return amount
            
def duplication_check(category, data):
    for x in data.keys():
        if category in x:
            return True
        else:
            return

def view_expense(data):
    for x, y in data.items():
        print(x + ": " + str(y))

def calculate_expense(data):
    total_expense = get_total_expense(data)
    average_expense = get_average_expense(data, total_expense)
    highest_expense = get_highest_expense(data)

    print("Total expense: ", total_expense)
    print("Average expense: ", average_expense)
    print("Highest expense: ", highest_expense)

def get_total_expense(data):
    total_expense = 0
    for x in data.values():
        for y in x: 
            total_expense += y
    return total_expense

def get_average_expense(data, total_expense):
    count = 0
    for x in data.values():
        for y in x:
            count += 1
    
    average_expense = total_expense / count
    return average_expense

def get_highest_expense(data):
    highest_expense = 0
    
    for x in data.values():
        for y in x:
            if y > highest_expense:
                highest_expense = y

    return highest_expense

def main():
    print(("=" * 50) + "\n")
    print("PERSONAL EXPENSE TRACKER\n")
    print(("=" * 50) + "\n")
    
    data = {}
    while True:
        service = get_user_choice()
        
        match service:
            case 1:
                add_expense(data)
            case 2:
                view_expense(data)
            case 3:
                calculate_expense(data)
            case 4:
                break

main()