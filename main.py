print("Welcome to simple calculator\n")

get_input_1 = int(input("Enter a number: "))

get_input_2 = int(input("Enter 2nd number: "))

def addition(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

arr_methods = [addition, subtract, multiply, divide]

choose_operand = int(input("0: Add, 1: Sub, 2: Multiply, 3: Divide = "))

operators = dict([
    (1, addition),
    (2, subtract),
    (3, multiply),
    (4, divide)
    ])

if choose_operand == 1:
    operators[1]