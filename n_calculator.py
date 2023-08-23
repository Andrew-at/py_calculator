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
Please Choose from the following operations:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Square Root
6. Prime Number
7. Quit
'''

print(calc_display)
print(operation_display)

operation_select = (input("Please select an operation: "))

if operation_select == 1:
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    print(number1 + number2)

elif operation_select == 2:
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    print(number1 - number2)

elif operation_select == 3:
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    print(number1 * number2)

elif operation_select == 4:
    number1 = int(input("Please enter the first number: "))
    number2 = int(input("Please enter the second number: "))
    print(number1 / number2)
    
elif operation_select == 5:
    number1 = int(input("Enter an integer to find the square root:"))
    print(sqrt(number1))

