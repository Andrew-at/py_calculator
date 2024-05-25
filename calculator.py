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
        print(operation_display)
        try:
            operation_select = int(input(">: "))
        except ValueError:
            print("Error, unknown value")

        if operation_select == 1:
            addition()

        elif operation_select == 2:
            subtraction()

        elif operation_select == 3:
            multiply()

        elif operation_select == 4:
            divide()

        elif operation_select == 5:
            sqrt()

        elif operation_select == 7:
            active = False

# add comments for everything/descriptions

def addition():
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    print(":", number1 + number2)

def subtraction():
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    print(":", number1 - number2)

def multiply():
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    print(":", number1 * number2)

def divide():
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    print(":", number1 / number2)

def sqrt():
    number1 = int(input("Enter a number to find the square root: "))
    print(":", math.sqrt(number1))

def evenOdd():
    number1 = int(input("Enter a number to find if it is even or odd: "))
    if number1 % 2 == 0:
        print(f"{number1} is even.")
    else:
        print(f"{number1} is odd")

print(calc_display)
input_select()
