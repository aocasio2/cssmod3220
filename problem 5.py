x = set(["apple,mango"])
y = set(["mango,orange"])
print(x)
print(y)

a = x & y
print("interaction = ", a)
z = x - y
print("difference = ", z)
b = y - x
print("difference = ", b)
c = z | b
print("the real difference =", c)
