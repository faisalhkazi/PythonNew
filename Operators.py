height = input("What is your height in CM?:").strip()
height = int(height)
bill = 0
if height >= 120:

    print("You can ride this rollercoaster")

    age = input("What is your age?: ").strip()
    age = int(age)

    if age <= 8:
        bill = 500
        print("Child Ticket is Rs: 500/-")
    elif age <= 18:
        bill = 700
        print("Youth Ticket is Rs: 700/-")
    elif age < 45:
        bill = 900
        print("Adult Ticket is Rs: 900/-")
    else:
        bill = 0

    photo = input("Do you want a photograph for you ride it will charge extra Rs 250/- ? Type y for yes and n for no: ")
    if photo == "y":
        bill += 250
        print(f"Your final bill is Rs: {bill}/-")
    elif photo == "n":
        bill = bill
        print(f"your final bill is {bill}")
    else:
        print("You entered the wrong input.")
else:
    print("Sorry you are small to ride this rollercoaster")
# ----------------------------------------------------------------------------------------------------
#
# Num = int(input("Type a number to check is it is even or odd: "))
#
# Num_check = int(Num % 2)
#
# if Num_check == 0:
#     print("This is the even number")
# else:
#     print("This is the odd number")

# ------------------------------------------------------------------------------------------------------