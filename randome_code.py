import random

# a = "Heads"
# b = "Tails"
#
# heads_or_tails = random.choice([a , b])
#
# print(heads_or_tails)

Random_Heads_or_Tails = random.randint(0 , 1)

if Random_Heads_or_Tails == 0:
    print("Heads")
else:
    print("Tails")