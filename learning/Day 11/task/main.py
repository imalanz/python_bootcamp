import random
from art import logo

def deal_card():
    """returns a card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def sum_score(list):
    """ take a list of cards and sum the values """
    if sum(list) == 21 and len(list) == 2:
        return 0
    if 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)

user_card = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_card.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:
user_score = sum_score(user_card)
computer_score = sum_score(computer_cards)
print(f"Your cards: {user_card}, current score: {user_score}")
print(f"Computer`s first card: {computer_score[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
else:
    keep_playing = input("Type 'y' to get another card, type 'n' to pass:")
    if keep_playing == 'y':
        user_card.append(deal_card())
    else:
        is_game_over = True

    want_to_play = input("do you want to play black jack? type 'y' or 'n':")


        card = random.choice(cards)
        your_hand.append(card)
        score += card
        print(f"Your cards: {your_hand}, current score: {score}")
        card = random.choice(cards)
        computer.append(card)
        computer_score += card
        print(f"Computer`s first card: {computer_score}")

        if score > 21:
            keep_playing = 'n'
            print("you went over. You lose")
        elif score > computer_score:
            print("you win!!")
        else:
            print("You lose")

    else:
        print(f"Your final hand: {your_hand}, final score: {score}")
        print(f"Computerś final hand: {computer}, final score: {computer_score}")
        if score > computer_score:
            print("you win!!")
        else:
            print("You lose")










