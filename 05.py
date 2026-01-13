# January 13, 2026

# Number Statistics Analyzer

# 1. Collects number from the user.
# 2. Process data (Average, Minimum, and Maximum)
# 3. Output data. 

def calculate_average(numbers):
    if not numbers:
        return
    else:
        total = 0
        for x in numbers:
            total += x
        average = total / len(numbers)
        return average 

def get_minimum(numbers):
    if not numbers:
        return
    else:
        minimum = numbers[0]
        for x in numbers:
            if minimum > x:
                minimum = x
        return minimum
    
def get_maximum(numbers):
    if not numbers:
        return 
    else: 
        maximum = numbers[0]
        for x in numbers:
            if maximum < x:
                maximum = x
        return maximum
    
def get_numbers():
    data = []
    while True:
        user_input = input("Input a number ('Q' if quit): ").strip().upper()
        if user_input == 'Q':
            break
        try:
            user_input = int(user_input)
        except ValueError:
            print("Invalid Input.")
        else:
            data.append(user_input)
    return data

numbers = get_numbers()

average = calculate_average(numbers)
minimum = get_minimum(numbers)
maximum = get_maximum(numbers)
print(f"Average: {average}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")