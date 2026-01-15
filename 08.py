#January 15, 2026

#Bank Account Manager (CLI) using OOP.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(amount):
        pass
    
    def withdraw(amount):
        pass
    
    def get_balance():
        pass 

def get_user_input():
    user_input = int(input("Enter: "))
    if user_input < 1 or user_input > 5:
            raise ValueError
    else:
        return user_input

def main():
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
            print("Invalid Input.")
        else:
            match user_input:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    break

main()