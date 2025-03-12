# score = 0
# height = 5.10
# is_winning = True
#
# print(f"You score is {score}, your height is {height} and are you winning = {is_winning}")
print("Welcome to the print calculator!")
Bill = float(input("What is your total bill amount? Rs:"))
Tip = float(input("How much tip do you like to give? In Percentage (10, 12, 14):"))
People = int(input("How manu people we have to split the bill? Rs: "))

Shares = (Bill + (Bill * (Tip / 100))) / People

print(f"Each person should pay Rs {round(Shares, 2)}") 