#Lloyd Higgins
#2023
#basic python calculator

import math

calc_display = '''
Welcome to my calculator!

 =======================
  _____________________
 |  _________________  |
 | |              0. | |
 | |_________________| |
 |  ___ ___ ___   ___  |
 | | 7 | 8 | 9 | | + | |
 | |___|___|___| |___| |
 | | 4 | 5 | 6 | | - | |
 | |___|___|___| |___| |
 | | 1 | 2 | 3 | | x | |
 | |___|___|___| |___| |
 | | . | 0 | = | | / | |
 | |___|___|___| |___| |
 |_____________________|

 =======================
'''

operation_display = '''
Please select an operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Square Root
6. Even or Odd
7. Quit
'''
print(calc_display)
print(operation_display)

def addition():
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    print(number1 + number2)

def subtraction():
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    print(number1 - number2)

def multiply():
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    print(number1 * number2)

def divide():
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    print(number1 / number2)

def sqrt():
    number1 = int(input("Enter a number to find the square root: "))
    print(math.sqrt(number1))

def evenOdd():
    number1 = int(input("Enter a number to find if it is even or odd: "))
    if number1 % 2 == 0:
        print(f"{number1} is even.")
    else:
        print(f"{number1} is odd")

operation_select = int
while operation_select != 7:
    operation_select = int(input(">: "))

    if operation_select == 1:
        addition()
        continue

    elif operation_select == 2:
        subtraction()
        continue
    
    elif operation_select == 3:
        multiply()
        continue
    
    elif operation_select == 4:
        divide()
        continue

    elif operation_select == 5:
        sqrt()
    
    elif operation_select == 6:
        evenOdd()
