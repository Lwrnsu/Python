#January 8, 2026

#Refactor Day 3's project, but using functions.

#Defines the variable to be used as container of user's data.
data = {}

#Function that validates the user's choice, returns bool depending on user's input.
def get_menu_choice(validation_type, user_input):
    
    if len(user_input.strip()) == 0:
        return False
    elif user_input.startswith('-'):
        return False
    
    match validation_type:
        case 'str':
            if not user_input.isdigit():
                return True
            else:
                return False
        case 'int':
            if user_input.isdigit():
                return True
            else:
                return False

#Function that add users, does not return anything
def add_user():
    #Validates wether the user_name is a character or not.
                name_validation = None
                while not name_validation:
                    user_name = input("Name: ")
                    
                    #Prevents the user to enter a number.
                    if get_menu_choice('str', user_name):
                        if user_name in data:
                            print("Name existed.")
                        else:
                            name_validation = True
                    else:
                        print("Invalid input, please try again.")
                
                #Validates wether user_age is a number or not.
                age_validation = None
                while not age_validation:
                    user_age = input("Age: ")
                    
                    if get_menu_choice('int', user_age):
                        user_age = int(user_age)
                        age_validation = True
                    else:
                        print("Invalid input, please try again.")
                
                user_status = None
                while user_status not in ("Y", "N"):
                    user_status = input("is active? [Y if yes, N if not]: ").upper()
                    match user_status:
                        case "Y":
                            user_status = True
                            break
                        case "N":
                            user_status = False
                            break
                        case _:
                            print("You did not enter valid input, please try again.")
                
                #Confirms if the details are correct.
                print("\nConfirm the following details: ")
                print(f"Name: {user_name}")
                print(f"Age: {user_age}")
                print(f"is Active: {user_status}")
                confirm_details = None
                while confirm_details not in ("Y", "N"):
                    confirm_details = input("Confirm? [Y if yes, N if not]: ").upper()
                    match confirm_details:
                        case 'Y':
                            data.update({f"{user_name}" : {"Age" : user_age, "Active" : user_status}})
                            break
                        case 'N':
                            print("Process interrupted.")
                            break
                        case _:
                            print("You did not enter valid input, please try again.")

#Function that prints the data, does not return anything.
def view_users():
    for x, val in data.items():
        print(x + ":")
        for y in val:
            print(f"\t{y}: {val[y]}")
            
#Defines the variable to be used as a user's decision. 
user_input = None

print("\n" + ("=" *50) + "\n") 
print("SIMPLE USER MANAGEMENT SYSTEM.")
print("\n" + ("=" *50))

while user_input != 3:
    
    #Determines the service based on the user's decision.
    print("\n1. Add an user.")
    print("2. View all user.")
    print("3. Exit")
    user_input = input("\nChoose a service: ")
    
    #Validates wether the user_input is a number or not.
    if get_menu_choice('int', user_input):
        user_input = int(user_input)
        
        match user_input:
            case 1:
                add_user()
            case 2:
                if len(data) > 0:
                   view_users()
                else: 
                    print("No users.")
            case 3:
                print("Exited the program.")
            case _:
                print("You did not enter valid input, please try again.")
    else:
        print("Invalid input, please try again.")
        
