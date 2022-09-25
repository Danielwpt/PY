print("Welcome to simple calculator\n")

get_input_1 = int(input("Enter a number: "))

get_input_2 = int(input("Enter 2nd number: "))

def addition(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

arr_methods = [addition, subtract, multiply]

choose_operand = int(input("0: Add, 1: Sub, 2: Multiply = "))

if arr_methods[choose_operand] == arr_methods[0]:
    print("Added together: " , addition(get_input_1, get_input_2))
elif arr_methods[choose_operand] == arr_methods[1]:
    print("Subs together: ", subtract(get_input_1, get_input_2))
else:
    print("Subs together: ", multiply(get_input_1, get_input_2))