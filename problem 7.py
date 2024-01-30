#problem 7

x = set ([1,2,3,4])
y = set ([4,5,6,7])
z = set ([8])
print(x)
print(y)
print(z)


#check if sets are disjoint
print("are x and y disjoint")
print(x.isdisjoint(y))

print("are x and y disjoint")
print(x.isdisjoint(z))

print("are x and y disjoint")
print(y.isdisjoint(z))
