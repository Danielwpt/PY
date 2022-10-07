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

choose_operand = int(input("1: Add, 2: Sub, 3: Multiply, 4: Divide = "))

operators = {
    1: addition,
    2: subtract,
    3: multiply,
    4: divide
}

if choose_operand == 1:
    sum = operators[1](get_input_1, get_input_2)
    print("Total: ", sum)
elif choose_operand == 2:
    sum = operators[2](get_input_1, get_input_2)
    print("Total: ", sum)
elif choose_operand == 3:
    sum = operators[3](get_input_1, get_input_2)
    print("Total: ", sum)
elif choose_operand == 4:
    sum = operators[4](get_input_1, get_input_2)
    print("Total: ", sum)
else:
    print("Nothing")