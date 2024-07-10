# Andrew-at
# 2023
# function for calculating square root of an int

"""
building the sqrt function from scratch without using Python
math library.
"""


def square_root():

    while True:
        try:
            num1 = int(input("Enter a number: "))
            break
        except ValueError:
            print("Error: unknown value")

    sqrt = num1 ** (1/2)
    print(sqrt)