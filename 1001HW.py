from random import randrange

for fre in range(1,6):
    fre1 = fre
    num = randrange(1,20)
    guess = int(input("num?"))

    if num == guess:
        print(f"That's right!You used {fre1} frequency(s)")
        break
    if guess < num:
        print("Too small~(～￣▽￣)～")
    if guess > num:
        print("Too big~(～￣▽￣)～")
    
