#January 5, 2025

#Ask for user's name and age.
user_name = input("What is your name: ")
user_age = int(input("What is your age: "))

#Determine if you are minor, adult, or senior citizen.
if user_age > 18 and user_age < 60:
    print(f"Hello {user_name}, you are adult!")
elif user_age >= 60:
    print(f"Hello {user_name}, you are senior!")
else: 
    print(f"Hello {user_name}, you are minor!")