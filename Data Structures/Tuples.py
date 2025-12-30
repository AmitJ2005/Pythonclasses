t1 = (1, 2, 3)
t2 = tuple((10.5,))
t3 = ("single",)
t4 = ()

print("t1:", t1)
print("t2:", t2)
print("t3:", t3)
print("t4:", t4)
print(type(t1), type(t2), type(t3), type(t4))

print("-----------------------------")

# Packing and unpacking
packed = 10, 20, 30, [40, 50]
a, b, c, d = packed
print(packed, a, b, c, d)
print(type(packed))
print(packed[3])

print("-----------------------------")

# Tuple methods: count and index
print(packed.count(20))
print(packed.index(30))

print("-----------------------------")


# Immutability: tuples cannot be changed in-place
try:
    packed[0] = 99
except TypeError as e:
    print("Immutability error:", e)

print("-----------------------------")

# You can, however, create new tuples by concatenation or repetition
new_tuple = packed + (99,)
print(new_tuple)
r = ("sambhavi", ) * 3
print(r)
print(type(r))

