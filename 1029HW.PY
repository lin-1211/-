from random import choice
name = ["Dog","Cat","Chicken"]
verb = ["bites","hits","takes"]
noun = ["pie","apple","ball"]

for num in range(0,4):
    nameSelect = choice(name)
    verbSelect = choice(verb)
    nounSelect = choice(noun)
    print(f"{nameSelect} {verbSelect} {nounSelect}.")
