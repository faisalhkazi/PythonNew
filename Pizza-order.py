# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25
# add_pepperoni = 2
# add_pepperoni_m_or_l = 3
# extra_cheese = 2
# bill = 0
#
# print("\n\n Welcome to the Python Pizza Store!!!")
# print("\n\nBelow are the charges for individual selection \n\n Small_pizza = 15 \n\n Medium_pizza = 20 \n\n Large_pizza = 25 \n\n Add_pepperoni = 2 \n\n Add_pepperoni_m_or_l = 3 \n\n Extra_cheese = 2")
#
# size = input("What size of Pizza you want? Small(s), Medium(m) or Large(l): ")
# pepperoni = input("Do you want pepperoni on Pizza? y or n: ")
# cheese = input("Do you want extra cheese on Pizza? y or n: ")
#
# if size == "s":
#     bill = small_pizza
#     if pepperoni == "y":
#         bill += add_pepperoni
#     else:
#         bill = bill
#     if cheese == "y":
#         bill += extra_cheese
#     else:
#         bill = bill
#     print(f"Your final bill is {bill}$")
#
# elif size == "m":
#     bill = medium_pizza
#     if pepperoni == "y":
#         bill += add_pepperoni_m_or_l
#     else:
#         bill = bill
#     if cheese == "y":
#         bill += extra_cheese
#     else:
#         bill = bill
#     print(f"Your final bill is {bill}$")
#
# elif size == "l":
#     bill = large_pizza
#     if pepperoni == "y":
#         bill += add_pepperoni_m_or_l
#     else:
#         bill = bill
#     if cheese == "y":
#         bill += extra_cheese
#     else:
#         bill = bill
#     print(f"Your final bill is {bill}$")
#
# else:
#     print("You entered the wrong inputs")

# ----------------------------------------------------------------------------------------------------------------------


print("\n\n Welcome to the Python Pizza Store!!!")
print("\n\nBelow are the charges for individual selection \n\n Small_pizza = 15 \n\n Medium_pizza = 20 \n\n Large_pizza = 25 \n\n Add_pepperoni = 2 \n\n Add_pepperoni_m_or_l = 3 \n\n Extra_cheese = 2")

size = input("What size of Pizza you want? Small(s), Medium(m) or Large(l): ")
pepperoni = input("Do you want pepperoni on Pizza? y or n: ")
cheese = input("Do you want extra cheese on Pizza? y or n: ")
bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("You have entered wrong input")

if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if cheese == "y":
    bill += 1

print(f"Your final bill is ${bill}")
