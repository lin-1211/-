from random import choice
name = ["Dog","Cat","Chicken"]
verb = ["bites","hits","takes"]
noun = ["pie","apple","ball"]

nameSelect = choice(name)
verbSelect = choice(verb)
nounSelect = choice(noun)

for num in range(0,4):
    print(f"{nameSelect} {verbSelect} {nounSelect}.")