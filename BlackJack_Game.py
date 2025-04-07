import art
import random

def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def sub(n1, n2):
    return n1 - n2

def division(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "*": multiply,
    "-": sub,
    "/": division,
}


Account_Balance = 1000

print(art.logo)
print("Welcome to the BlackJack Game!!!")

bid_amount = [10, 20, 50, 100, 200, 500]

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


random.choice(cards)


def start_game():
    for num in bid_amount:
        print(num)
    bid_p = int(input("Enter the bid amount\n"))

    if bid_p not in bid_amount:
        print("This is the invalid bid")
        exit()
    if bid_p > Account_Balance:
        print("You don't have enough balance")
        exit()
    return bid_p

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Blackjack
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare(player_score, dealer_score):
    if player_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21 or player_score > dealer_score:
        return "You win 🥳"
    elif player_score < dealer_score:
        return "You lose 😭"
    else:
        return "Draw 🙃"

def play_blackjack():
    global Account_Balance
    bid = start_game()

    player_cards = [random.choice(cards), random.choice(cards)]
    dealer_cards = [random.choice(cards), random.choice(cards)]
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Dealer first card: {dealer_cards[0]}")



    game_over = False
    while not game_over:
        should_continue = input("Type 'hit' to draw another card, 'stand' to hold: ").lower()
        if should_continue == "hit":
            player_cards.append(random.choice(cards))
            print(f"Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
            if calculate_score(player_cards) > 21:
                print("You went over 21. You lose 😭")
                Account_Balance -= bid
                game_over = True
        else:
            game_over = True



    while calculate_score(dealer_cards) < 17:
            dealer_cards.append(random.choice(cards))
            print(f"Dealer Cards: {dealer_cards}, scores: {calculate_score(dealer_cards)}")



    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    print(compare(player_score, dealer_score))

    if compare(player_score, dealer_score) == "You win 🥳":
        Account_Balance += bid
    elif compare(player_score, dealer_score) == "You lose 😭":
        Account_Balance -= bid

    print(f"Your current balance is: {Account_Balance}")

while True:
    start_game1 = input("Type 'start' to begin the game or 'exit' to quit: ").lower()
    if start_game1 == "start":
        play_blackjack()
        again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
        if again != "yes":
            print("THank you for playing Blackjack. Bye Bye!!!")
            break
    else:
        print("Thanks for playing BlackJack!")
        break
