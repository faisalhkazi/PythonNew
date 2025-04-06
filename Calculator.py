def add(n1, n2):
    return n1 + n2

def sub(n3, n4):
    return n3 - n4

def multi(n5, n6):
    return n5 * n6

def div(n7, n8):
    return n7 / n8

Addition = add
Subtraction = sub
Multiplication = multi
Division = div

operators = {
    '+': Addition,
    '-': Subtraction,
    '*': Multiplication,
    '/': Division
}

print(operators["*"](4, 8))

# user_input = float(input("Your first number\n"))
# select_operators = input("Select the operation you want to perform (a choice of '+', '-', '*' or '/')\n")
# user_input2 = float(input("Your second number\n"))

result = 0

def mathematical_operation():
    global result
    user_input = float(input("Your first number\n"))
    print("Select from the below operators: ")
    for symbol in operators:
        print(symbol)
    select_operators = input("Select the operation you want to perform (a choice of '+', '-', '*' or '/')\n")
    user_input2 = float(input("Your second number\n"))

    if select_operators == "+":
        result = round(operators["+"](user_input, user_input2), 2)
        print(f"{user_input} {select_operators} {user_input2} = {result}")
    elif select_operators == "-":
        result = round(operators["-"](user_input, user_input2), 2)
        print(f"{user_input} {select_operators} {user_input2} = {result}")
    elif select_operators == "*":
        result = round(operators["*"](user_input, user_input2), 2)
        print(f"{user_input} {select_operators} {user_input2} = {result}")
    elif select_operators == "/":
        result = round(operators["/"](user_input, user_input2), 2)
        print(f"{user_input} {select_operators} {user_input2} = {result}")
    else:
        print("Invalid operator. Please try again")
        mathematical_operation()
    return result

def continue_operations():
    global result
    print("Select from the below operators: ")
    for symbol in operators:
        print(symbol)
    select_operators = input("Select the operation you want to perform\n")
    new_input = float(input("Your new number\n"))
    if select_operators == "+":
        result = round(operators["+"](result, new_input))
        print(f"{result} {select_operators} {new_input} = {result}")
    elif select_operators == "-":
        result = round(operators["-"](result, new_input))
        print(f"{result} {select_operators} {new_input} = {result}")
    elif select_operators == "*":
        result = round(operators["*"](result, new_input))
        print(f"{result} {select_operators} {new_input} = {result}")
    elif select_operators == "/":
        result = round(operators["/"](result, new_input))
        print(f"{result} {select_operators} {new_input} = {result}")
    return result



mathematical_operation()

# continue_working = input("You want to continue with calculator. Press 'yes' or 'no'".lower() )

while True:
    continue_working = input("You want to continue with calculator. Press 'yes' or 'no' and 'Exit' to terminate the calculator session\n".lower())

    if continue_working == "yes":
        continue_operations()
    elif continue_working == "no":
        mathematical_operation()
    elif continue_working == "exit":
        print("Thank you for using the calculator. Bye Bye!")
        break
    else:
        print("Invalid entry")