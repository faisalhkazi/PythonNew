import random

fruits = ["Apple", "Banana", "Cherry", "Mango", "Grapes", "Orange", "Pineapple", "Strawberry", "Watermelon", "Papaya"]

selected_fruit = random.choice(fruits)
hidden_fruit = "_" * len(selected_fruit)
print(hidden_fruit)

print("This is the blank field which is any fruit which you have to guess")
user_input = input("Type any one Alphabet which will be the part of the fruit\n")

if user_input 