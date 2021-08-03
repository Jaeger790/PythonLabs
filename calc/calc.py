
import pandas as pd
import numpy as np
import matplotlib  as plot

def add(x , y):
  return x + y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def instructions():
   return print('Select an operation: +, -, *, /' '\n'
             'subtraction: 1' '\n'
             'addition: 2' '\n'
             'multiplication: 3' '\n'
             'division: 4')

instructions()

def selection():
   
    input('Enter choice: ' )
    
selection()

if selection in ('1', '2', '3', '4'):
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))

    if selection.choice == '1':
        print(num1, '-', num2, '=', subtract(num1, num2))
    elif choice == '2':
        print(num1, '+', num2, '=', add(num1, num2))
    elif choice == '3':
        print(num1, '*', num2, '=', multiply(num1, num2))
    elif choice == '4':
        print(num1, '/', num2, '=', divide(num1, num2))
    
else:
    print('Invalid input')

Keep_going = input('do you want to continue?  (y/n): ')

while Keep_going == 'y':
  selection()
   
   


  #