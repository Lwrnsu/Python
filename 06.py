#January 13, 2026

#More like a debugging session.

# Employee Salary Analyzer
def get_employee():
    while True:
        val = input("How many employees: ")
        try:
            val = int(val)
        except ValueError:
            print("Invalid Input")
        else:
            if val <= 0:
                print("Can't be lower than 1.")
            else: 
                return val

def get_employee_name():
    while True:
        val = input("Enter employee name: ")
        
        if not val:
            print("Invalid Input.")
        else:
            return val

def get_employee_salary(name):
    while True:
        val = input(f"Enter salary for {name}: ")
    
        if not val:
            print("Invalid Input.")
        
        try:
            val = float(val)
        except ValueError:
            print("Invalid salary entered!")
        else:
            return val

def get_average_salary(employees):
    total_salary = 0
    for x in employees:
        total_salary += employees[x]
    return total_salary / len(employees)

def program_output(average_salary, employees):
    print("Employee Salaries: ")
    for x in employees:
        print(x, employees[x])
    print("Average Salary: ", average_salary)

employees = {}

while True:
    num_employees = get_employee()
    if num_employees:
        break

for i in range(num_employees):
    name = get_employee_name()
    salary = get_employee_salary(name)
    employees.update({name : salary})

average_salary = get_average_salary(employees)
program_output(average_salary, employees)