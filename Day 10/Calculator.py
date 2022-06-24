# Calculator
from replit import clear


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def ask_for_first_number():
    return int(input("Type first number: "))

def ask_for_operation():
    return input("What operation should be done? ( + , - , * , / )")

def ask_for_second_number():
    return int(input("Type second number: "))

run_program = True

first_number = ask_for_first_number()

while run_program:
    operation = ask_for_operation()
    second_number = ask_for_second_number()
    result = 0

    if operation == "+":
        result = add(first_number, second_number)
        print(f"Result of adding {first_number} and {second_number} is {result}")
    elif operation == "-":
        result = subtract(first_number, second_number)
        print(f"Result of subtracting {second_number} from {first_number} is {result}")
    elif operation == "*":
        result = multiply(first_number, second_number)
        print(f"Result of multiply {first_number} by {second_number} is {result}")
    elif operation == "/":
        result = divide(first_number, second_number)
        print(f"Result of dividing {first_number} by {second_number} is {result}")
    else:
        print("No such operation")
    
    should_continue = input("Do you want to continue with current number? Or program should end? (y/n)")

    first_number = result

    if should_continue == "n":
        run_program = False
    else:
        clear()

