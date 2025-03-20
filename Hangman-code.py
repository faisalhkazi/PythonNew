import random

h1 = r''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |        
| |        
| |    
| |     
| |   
| |         
| |          
| |          
| |          
| |         
""""""""""|_         |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .
'''

h2 = r''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |         Y . . Y
| |          |   | 
| |          | . |  
| |          |   |   
| |          
| |          
| |          
| |         
| |         
""""""""""|_         |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .
'''

h3 = r''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y
| |       // |   | 
| |      //  | . |  
| |     ')   |   |   
| |          
| |          
| |          
| |          
| |         
""""""""""|_         |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .
'''

h4 = r''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          
| |          
| |          
| |         
| |         
""""""""""|_         |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .
'''

h5 = r''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'
| |          || 
| |          || 
| |          || 
| |         / | 
""""""""""|_`-'      |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .
'''

h6 = r''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`  Game Over !!!!!!!
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .
'''
fruits = ["Apple", "Banana", "Cherry", "Mango", "Grapes", "Orange", "Pineapple", "Strawberry", "Watermelon", "Papaya"]
selected_fruit = random.choice(fruits).lower()
images = [h1, h2, h3, h4, h5, h6]
hidden_word = ["_" for _ in selected_fruit]

lifeline = 6
guess_letters = set()

print("Guess the fruit! You have 6 lifelines.")
print(" ".join(hidden_word))

while lifeline > 0:
    guess = input("Enter the letter: ").lower()

    if guess in guess_letters:
        print("You have already entered this letter! Please try again")
        continue

    guess_letters.add(guess)

    if guess in selected_fruit:
        for i in range(len(selected_fruit)):
            if selected_fruit[i] == guess:
                hidden_word[i] = guess
        print("Correct Guess")

    else:
        lifeline -= 1
        print(f"Wrong guess! Lifeline left= {lifeline}")
        print(images[5 - lifeline])

    print(" ".join(hidden_word))

    if "_" not in hidden_word:
        print("Congratulation! You guessed the correct fruit. You win")
        break

else:
    print("You Lost! Game over")



