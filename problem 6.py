#problem 6

x = set(["apple,mango"])
y = set(["mango,orange"])
z = set(["mango"])

print(x)
print(y)
print(z)

#check for subset
print("is x a subset of y")
print(x.issubset(y))

print("is x a subset of y")
print(y.issubset(x))

print("is x a subset of y")
print(x.issubset(z))

print("is x a subset of y")
print(z.issubset(x))

print("is x a subset of y")
print(y.issubset(z))

print("is x a subset of y")
print(z.issubset(y))

