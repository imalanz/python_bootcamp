import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

imanol = int(input("what do you choose? type 0 for rock, 1 for paper and 2 for scissors"))
computer = random.choice(list)

if computer == 0 and imanol == 1:
    print("you win:")
else:
    print("you lose")

if computer == 1 and imanol == 2:
    print("you win")
else:
    print("you lose")

if computer == 2 and imanol == 0:
    print("you win")
else:
    print("you lose")

print("computer chose:")
print(computer)

if imanol == scissors:
    if computer == rock:
        print("you lose")
    if computer == paper:
        print("you win")
    else:
        print("tie")
elif imanol == paper:
    if computer == rock:
        print("you win")
    elif computer == paper:
        print("tie")
    else:
        print("you win")
elif imanol == rock:
    if computer == rock:
        print("tie")
    elif computer == paper:
        print("you lose")
    else:
        print("you win")

