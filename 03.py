#January 7, 2025

#Use Dictionary to store users. 
#Each users has: name, age, and active status.
#Program allows: add user, view all user, and prevent duplicate names.
#Must use: Loop, Dictionary, Input Validation, and Clean variable naming.



#Defines the variable to be used as container of user's data.
data = {}

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
    if user_input.isdigit():
        user_input = int(user_input)
        match user_input:
            case 1:
                #Validates wether the user_name is a character or not.
                name_validation = None 
                while not name_validation:
                    user_name = input("Name: ")
                    
                    #Prevents user to enter a blank.
                    if len(user_name.strip()) == 0: 
                        print("Invalid input, please try again.")
                    
                    #Prevents the user to enter a number.
                    elif not user_name.isdigit():
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
                    
                    #Prevents user to enter a blank.
                    if len(user_age.strip()) == 0: 
                        print("Invalid input, please try again.")
                    
                    #Prevents user to enter a character
                    elif user_age.isdigit():
                        user_age = int(user_age)
                        age_validation = True
                    else:
                        print("Invalid input, please try again.")
                
                user_status = None
                while user_status != "Y" or user_status != "N":
                    user_status = input("is active? [Y if yes, N if not]: ").upper()
                    match user_status:
                        case "Y":
                            print("True")
                            user_status = True
                            break
                        case "N":
                            print("False")
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
                while confirm_details != 'Y' or confirm_details != 'N':
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
            case 2:
                if len(data) > 0:
                    for x, val in data.items():
                        print(x + ":")
                        for y in val:
                            print(f"\t{y}: {val[y]}")
                else: 
                    print("No users.")
            case 3:
                print("Exited the program.")
            case _:
                print("You did not enter valid input, please try again.")
    else: 
        print("Invalid input, please try again.")