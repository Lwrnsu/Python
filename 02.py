#January 7, 2025. 

#It Defines the variable to be use in while loop.
user_input = ''

#The program itself, doesn't run if the user inputs "exit".
while user_input.upper() != 'EXIT':
    user_input = input('\nEnter a number: ')
    
    #It checks wether the user_input is a string or a number.
    if not user_input.isdigit():
        if user_input.upper() == "EXIT":
            print("You've exited the program.")
            break
        else:
            print("You've inputted a String!")
    else:
       numeric_value = int(user_input)
       if numeric_value % 3 == 0 and numeric_value % 5 == 0:
            print('FizzBuzz')
       elif numeric_value % 3 == 0:
            print('Fizz')
       elif numeric_value % 5 == 0:
            print('Buzz')
       else:
            print('The number is not divisible by 3 or 5.')
    
    print('If you wish to exit, enter "exit".')