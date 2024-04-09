# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:37:31 2024

@author: Jordan
"""
import math
import time

def calculator():
    num1 = int(input("x ? x =\n^\nEnter your first number:\t\t "))
    operator = input(f"{num1} ? x =\n  ^\nEnter the operator (+ - / *):\t ")
    sqrt_keys = ['sq', '√', 'root', 'squared', 'sqrt']

    for key in sqrt_keys:
        if operator == key:
            operator = 'sqrt'
            break

    if operator != 'sqrt':
        num2 = int(input(f"{num1} {operator} x =\n    ^\nEnter your second number:\t\t "))
    else:
        num2 = 1

    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2,
        '^': num1 ** num2,
        '//': num1 // num2,
        '%': num1 % num2,
        'sqrt': math.sqrt(num1)
    }

    if operator in operations:
        result = operations[operator]
        print(f"{num1} {operator} {num2} = {result} \n")
    else:
        print(f"{num1} {operator} {num2} =\n    ^\nError: {operator} is an unknown operator")

    time.sleep(1.5)
    print("PRESS CONTROL-C TO QUIT (command C)\n__________________________________")

while True:
    calculator()