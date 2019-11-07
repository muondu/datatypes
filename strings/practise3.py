import random


a = input("Enter a number from 0 to 5:   ")

b = random.randrange(0,5)


if a == b:
    print("You got the write number.Yeah!")
else:
    print("Try again")
    print(b)