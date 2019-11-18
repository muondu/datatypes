a = ("Nesh","Malli","Frank")
print(a)
x = ("Mango","Pineaple","Passion")
print(x)
y = list(x)
y[2] = "Banana"
x = tuple(y)

print(x)
c = a + x
print(c)
print(len(c))

if "Mango" in c:
    print("Yes, the item exists")
