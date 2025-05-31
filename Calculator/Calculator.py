from calculator_imports import logo
import os

def clear_console():
    os.system('clear')

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    n1 = float(input("Please type the first number: "))
    while True:
        for symbol in operations:
            print(symbol)
        operator = input("Choose a mathematical operator from the above choices: ")
        if not operator in operations:
            print("Invalid operator!")
        n2 = float(input("Please type the second number: "))
        result = operations[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {result}")
        
        continue_working = input("To continue working with the result press 'y'. To clear and begin again, press 'n'. ")
        if continue_working == "y":
            n1 = result
        elif continue_working == "n":
            clear_console()
            n1 = float(input("Please type the first number: "))
        else:
            print("Invalid input!")

calculator()