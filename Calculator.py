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

def mathematical_operation():
    user_input = float(input("Your first number\n"))
    print("Select from the below operators: ")
    for symbol in operators:
        print(symbol)
    select_operators = input("Select the operation you want to perform (a choice of '+', '-', '*' or '/')\n")
    user_input2 = float(input("Your second number\n"))

    if select_operators == "+":
        print(round(operators["+"](user_input, user_input2), 2))
    elif select_operators == "-":
        print(round(operators["-"](user_input, user_input2), 2))
    elif select_operators == "*":
        print(round(operators["*"](user_input, user_input2), 2))
    elif select_operators == "/":
        print(round(operators["/"](user_input, user_input2), 2))
    else:
        print("Invalid operator. Please try again")
        mathematical_operation()

mathematical_operation()

# continue_working = input("You want to continue with calculator. Press 'yes' or 'no'".lower() )

while True:
    continue_working = input("You want to continue with calculator. Press 'yes' or 'no'\n".lower())

    if continue_working == "yes":
        mathematical_operation()
    elif continue_working == "no":
        print("Thank you for using the Calculator".title())
        break
    else:
        print("Invalid entry")