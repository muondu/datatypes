import random

character = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*:;"
length = input("Enter password length:  ")

length = int(length)
password = ""
for nesh in range(length):
    password += random.choice(character)
print(password)