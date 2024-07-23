# Andrew-at
# 2023
# basic python console calculator

"""
This is a side project using some
beginner Python fundamentals (loops, error checking, ect.)
to build a calculator that uses a terminal window.
The ultimate goal is to recreate some math functions from the Python
math library.
"""

from pathlib import Path
from math_functions import *

# displays a calculator ascii graphic
txt_path1 = Path('calc_display.txt')
calc_display = txt_path1.read_text()

# displays operations in console via .txt file
txt_path2 = Path("operation_display.txt")
operation_display = txt_path2.read_text()


# operation select
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
            square_root()
        elif operation_select == 6:
            even_odd()
        elif operation_select == 0:
            active = False


print(calc_display)
input_select()
