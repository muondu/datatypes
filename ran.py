import random


w = input("Enter a number between 0 and 5   ")
x = random.randrange(0,5 )

if w == x:
    print("You won")
else:
    print("You loose")

print(x)