#January 15, 2026

#Bank Account Manager (CLI) using OOP.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount < 1:
            raise ValueError
        else:
            self.__balance += amount
    
    def withdraw(amount):
        pass
    
    def get_balance(self):
        return self.__balance

def create_account(accounts):
    while True:
        user_name = input("Name: ").strip()
        if not user_name:
            print("Invalid Name.")
        else:
            accounts.append(BankAccount(f"{user_name}"))
            break

def account_list(accounts):
    count = 0
    for x in accounts:
        count += 1
        print(f"{count}. {x.owner}")
    return count

def get_account(count):
    minimum = (count - count) + 1
    maximum = count
    user_input = int(input("Enter: "))
    if user_input < minimum or user_input > maximum:
            raise ValueError

def get_amount():
    user_amount = int(input("Enter amount: "))
    if user_amount < 1: 
        raise ValueError
    else: 
        return user_amount

def deposit(accounts):
    while True:
        try:
            account = get_account(account_list(accounts))
        except ValueError:
            print("Invalid Input.")
        else:
            try:
                amount = get_amount()
            except ValueError:
                print("Invalid Input.")
            else:
                try:
                    accounts[account].deposit(amount)
                except ValueError:
                    print("Invalid amount.")
                else:
                    break

def check_balance(accounts):
    while True:
        try:
            account = get_account(account_list(accounts))
        except ValueError:
            print("Invalid Input.")
        else:
            print(accounts[account].get_balance())

def get_user_input():
    user_input = int(input("Enter: "))
    if user_input < 1 or user_input > 5:
            raise ValueError
    else:
        return user_input

def main():
    accounts = []
    print(("=" * 50) + "\n")
    print("BANK ACCOUNT MANAGER\n")
    print("=" * 50)

    while True:
        print("\nServices: ")
        print("\n1. Create an account.")
        print("2. Deposit.")
        print("3. Withdraw.")
        print("4. Check Balance.")
        print("5. Exit.\n")
        try:
            user_input = get_user_input()
        except ValueError:
            print("\nInvalid Input.")
        else:
            match user_input:
                case 1:
                    create_account(accounts)
                case 2:
                    deposit(accounts)
                case 3:
                    pass
                case 4:
                    check_balance(accounts)
                case 5:
                    break

main()