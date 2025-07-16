print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip = (tip / 100) + 1
total_with_tip = bill * tip

by_person = total_with_tip / people

print(f"total by person will be {by_person}")