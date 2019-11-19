import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
password = input("Enter your password length : ")

password = int(password)
nesh = ""
for length in range(password): 
    nesh += random.choice(letters)
print(nesh)