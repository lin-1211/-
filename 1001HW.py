from random import randrange
num = int(randrange(1,20))
for fre in range(1,6):
    guess = int(input("num?"))
    
    if num == guess:
        print(f"That's right!You used {fre} frequency(s)")
        break
    elif guess < num:
        print("Too small~(～￣▽￣)～")
    elif guess > num:
        print("Too big~§(*￣▽￣*)§")

