print("Write names of animals")
set1 = {"Lion"}
print(set1)
set1.add(input("Enter your first word:   "))
set1.update([input("Enter your second word:  ")])
set1.add(input("Enter your third word:  "))
set1.update([input("Enter your fourth word:  ")])
set1.add(input("Enter your last word:  "))
set1.remove(input("Enter any word you want to remove:  "))
print(set1)
print("This is the length of what you have writtten:  ")
print(len(set1))




print("Write names of people")
set2 = {"Jef"}
print(set2)
set2.add(input("Enter your first word:   "))
set2.update([input("Enter your second word:  ")])
set2.add(input("Enter your third word:  "))
set2.update([input("Enter your fourth word:  ")])
set2.add(input("Enter your last word:  "))
set2.remove(input("Enter any word you want to remove:  "))
print(set2)
print("This is the length of what you have writtten:  ")
print(len(set2))

print("This is the result when the two list are put together")

set3 = set1.union(set2)
print(set3)