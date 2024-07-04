# Andrew-at
# 2023
# basic python console calculator

import math
from pathlib import Path

# displays the a calculator ascii graphic
txt_path1 = Path('calc_display.txt')
calc_display = txt_path1.read_text()

# displays operations in console via .txt file
txt_path2 = Path("operation_display.txt")
operation_display = txt_path2.read_text()

# operation select for calculator
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
        elif operation_select == 2:
            subtract()
        elif operation_select == 3:
            multiply()
        elif operation_select == 4:
            divide()
        elif operation_select == 5:
            sqrt()
        elif operation_select == 6:
            even_odd()
        elif operation_select == 7:
            break

# functions for adding multiple integers
# 0 input = 0
# 1: addition
def addition():

    num_list = []
    while True:

        try:
            num_range = int(input("How many numbers do you want to add? "))
            break
        except ValueError:
            print("Error: unknown value")

    for i in range(num_range):
        while True:
            try:
                num = int(input("select a number: "))
                num_list.append(num)
                break
            except ValueError:
                print("Error: unknown value")

    print(sum(num_list))

# 2: subtract
def subtract():
    while True:
        try:
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter a number to subtract by: "))
            break
        except ValueError:
            print("Error: unknown value")
    print(":", num1 - num2)

# 3: multiply
def multiply():
    number1 = int(input("Choose a number to multiply: "))
    number2 = int(input("Enter number of times to multiply: "))
    print(":", number1 * number2)

# 4: divide
def divide():
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    print(":", number1 / number2)

# 5: sqrt
def sqrt():
    number1 = int(input("Enter a number to find the square root: "))
    print(":", math.sqrt(number1))

# 6: even/odd comparison
def even_odd():
    number1 = int(input("Enter a number to find if it is even or odd: "))
    if number1 % 2 == 0:
        print(f"{number1} is even.")
    else:
        print(f"{number1} is odd")

print(calc_display)
input_select()
