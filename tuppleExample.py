numberTuple = (1, 2, 3)

print(numberTuple)
x = numberTuple[0]
y = numberTuple[1]
z = numberTuple[2]
print(x * y * z)

x, y, z = numberTuple  # same as above
print(x * y * z)

print(numberTuple.index(2))
print(numberTuple.count(1))
