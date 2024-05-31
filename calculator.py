# Andrew-at
# 2023
# basic python console calculator

import math
from pathlib import Path

txt_path1 = Path('calc_display.txt')
calc_display = txt_path1.read_text()

txt_path2 = Path("operation_display.txt")
operation_display = txt_path2.read_text()

def input_select():

    operation_select = int
    active = True
    while active:

        try:
            print(operation_display)
            operation_select = int(input(">: "))
        except ValueError:
            print("Error, unknown value")

        if operation_select == 1:
            addition()


# functions for two integers
# addition
def addition():

    while True:

        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            break
        except ValueError:
            print("Error: unknown value")

    print(":", num1 + num2)


# subtract
def subtract():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            break
        except ValueError:
            print("Error: unknown value")
    print(":", num1 - num2)

"""
# multiply
def multiply():
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    print(":", number1 * number2)

# divide
def divide():
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    print(":", number1 / number2)

# sqrt
def sqrt():
    number1 = int(input("Enter a number to find the square root: "))
    print(":", math.sqrt(number1))

# even or odd comparison
def evenOdd():
    number1 = int(input("Enter a number to find if it is even or odd: "))
    if number1 % 2 == 0:
        print(f"{number1} is even.")
    else:
        print(f"{number1} is odd")
"""
print(calc_display)
input_select()
