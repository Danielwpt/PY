print("Welcome to simple calculator\n")

get_input_1 = int(input("Enter a number: "))

get_input_2 = int(input("Enter 2nd number: "))

def addition(x, y):
    return x + y

arr_methods = [addition]

print("Added together: ",  arr_methods[0](get_input_1, get_input_2))