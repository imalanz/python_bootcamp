from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!")
difficulty = input("Guess a difficulty. Type 'easy' or 'hard': ")

tries = 5
if difficulty == 'easy':
    tries = 10

number = random.randint(0, 100)
while tries > 0:
    print(f"You have {tries} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print("You win")
        tries = 0
    elif guess > number:
        print("Too high")
        tries -= 1
    else:
        print("Too low")
        tries -=1
