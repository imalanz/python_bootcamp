# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


from art import logo
print(logo)






other_users = True
nombres = {}
while other_users:
    name = str(input("whats your name: \n"))
    bid = int(input("whats your bind: \n$"))

    nombres[name] = bid

    other_users = input("are there other users that wants to join?\n")
    if other_users == "no":
        other_users = False


for key in nombres:
    nombres[key]