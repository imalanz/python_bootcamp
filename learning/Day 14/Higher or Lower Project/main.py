import random
from game_data import data
from art import logo, vs

def compare(guess):
    comparation = {"a": a, "b": b,}
    if guess == "a":
        comparing = comparation["b"]
    else:
        comparing = comparation["a"]

    if comparation[guess]['follower_count'] > comparing["follower_count"]:
        return True
    else:
        return False


print(logo)

shuffle_list = random.shuffle(data)

index = 0
continue_playing = True
while continue_playing:
    try:
        a = data[index]
        b = data[index + 1]

        print(f"Compare A: {a['name']}, {a['description']}, {a['country']}\n{a['follower_count']}")
        print(f"{vs}\n")
        print(f"Compare B: {b['name']}, {b['description']}, {b['country']}\n{b['follower_count']}")

        guess = input("who has more followers? Type 'A' or 'B':   ").lower()

        continue_playing = compare(guess)
        if continue_playing == True:
            index += 1
            print(logo)
            print(f"Youre right! Current score: {index}")
        else:
            print(f"Sorry, thats wrong. Final score: {index}")
    except IndexError:
        index = index * -1




# check the index of selected and deleted from list so it wont repeat

#chose random artist

#compare A to B

# chose one of them

# if selected is right == you win and add score += 1

# and repeat

