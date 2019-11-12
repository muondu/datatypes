#Import time
import time
a = "Opps! We have an unwanted word in our list"
print(a)
time.sleep(2)

b = ["Bugatti","BMW","Jaguar","Cow","Subaru"]
print(b)       

time.sleep(3)

c = "Let as remove the unwanted word in our list: "
print(c)

time.sleep(1)

d = b.remove(input("Enter the wrong one:  "))

time.sleep(1)

print(b)

e = b.append(input("Enter the write thing:  "))

print(b)
