numberTupple = (1, 2, 3)

print(numberTupple)
x = numberTupple[0]
y = numberTupple[1]
z = numberTupple[2]
print(x * y * z)

x, y, z = numberTupple  # same as above
print(x * y * z)

print(numberTupple.index(2))
print(numberTupple.count(1))
