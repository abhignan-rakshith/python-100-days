# Calculator
import os
from art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2
# Divide
def divide(n1, n2):
    return n1 / n2

def exponent(n1, n2):
    return n1 ** n2

operations = {
    '+': add, 
    '-': subtract, 
    '*': multiply, 
    '/': divide,
    '^': exponent,
}

# Recursion Concept (Starting from first)
# Don't use them if you have no checking code, if not you'll get an infinite loop!
def calculator():
    print(logo)
    
    n1 = float(input("What's the first number?: "))
    for symbols in operations:
        print(symbols)
        
    again = 'y'
    while again == 'y':
        operation_symbol = input("Pick an operation to perform from the above list: ")
        n2 = float(input("What's the next number?: "))
        
        function = operations[operation_symbol]
        answer = function(n1, n2)
        
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new.: ")
        if again == 'y':
            n1 = answer
        elif again == 'n':
            os.system('cls')
            calculator()

calculator()