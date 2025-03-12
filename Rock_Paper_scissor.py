import random

Rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = r'''     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors = r'''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_list = [Rock, Paper, Scissors]
random_selection = random.randint(0, 2)

computer = game_list[random_selection]

while True:

    user_input = input("What do you choose? Type 0 for Rock, Type 1 for Paper and type 2 for Scissors. \n")

    if user_input.lower() == "exit":
        print("Thank you for playing! Goodbye.")
        break

    if user_input == "0":
        print(Rock)
        print("Computer Selection")
        print(computer)
        if computer == Rock:
            print("Its a draw!")
        if computer == Paper:
            print("You Lose!")
        if computer == Scissors:
            print("You Win!")
    elif user_input == "1":
        print(Paper)
        print("Computer Selection")
        print(computer)
        if computer == Rock:
            print("You Win!")
        if computer == Paper:
            print("Its a draw!")
        if computer == Scissors:
            print("You Lose!")
    elif user_input == "2":
        print(Scissors)
        print("Computer Selection")
        print(computer)
        if computer == Rock:
            print("You Lose!")
        if computer == Paper:
            print("You Win!")
        if computer == Scissors:
            print("Its a draw!")

    else:
        print("You typed an invalid number. You lose!")


