#January 7, 2025. 

#Defined the variable to be use in while loop. 
user_input = '';

#Determines the output of the user. 
while user_input != 'exit':
    user_input = input('Enter a number: ')
    if int(user_input) % 3 == 0 and int(user_input) % 5 == 0:
        print('FizzBuzz')
    elif int(user_input) % 3 == 0:
        print('Fizz')
    elif int(user_input) % 5 == 0:
        print('Buzz')