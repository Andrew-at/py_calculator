# Andrew-at
# 2023
# function for calculating square root of an int

"""
math functions for the calculator file.
"""


# 1: Addition of multiple integers
def addition():

    num_list = []
    sum_total = 0

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

    for i in num_list:
        sum_total += i

    return sum_total


# 2:
# Subtraction
def subtract():

    while True:
        try:
            num1 = int(input("Enter a number: "))
            break
        except ValueError:
            print("Error: unknown value")

    while True:
        try:
            num2 = int(input("Enter a number to subtract by: "))
            break
        except ValueError:
            print("Error: unknown value")

    print(":", num1 - num2)


# 3: multiply
def multiply():

    while True:
        try:
            num1 = int(input("Enter a number: "))
            break
        except ValueError:
            print("Error: unknown value")

    while True:
        try:
            num2 = int(input("Enter number to multiply by: "))
            break
        except ValueError:
            print("Error: unknown value")

    print(":", num1 * num2)


# 4: divide
def divide():
    while True:
        try:
            num1 = int(input("Enter a number: "))
            break
        except ValueError:
            print("Error: unknown value")

    while True:
        try:
            num2 = int(input("Enter number to multiply by: "))
            break
        except ValueError:
            print("Error: unknown value.")

    if num2 == 0:
        print("Error: division by zero.")
    else:
        print(":", num1 / num2)


# 5: Square root
def square_root():

    while True:
        try:
            num1 = int(input("Enter a number: "))
            break
        except ValueError:
            print("Error: unknown value")

    sqrt = num1 ** (1/2)
    print(sqrt)


# 6: Even/Odd
def even_odd():

    while True:
        try:
            num1 = int(input("Enter a number: "))
            break
        except ValueError:
            print("Error: unknown value")

    if num1 % 2 == 0:
        print(f"{num1} is even.")
    else:
        print(f"{num1} is odd.")
