import random

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#random number
print(random.randrange(1,100))

#You cannot convert complex numbers into another number type.
d =int(z)
print(d)
print(type(d))
