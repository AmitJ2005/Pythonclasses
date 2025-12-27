# Creating lists


empty = []
print(empty)

# 2. Literal list with values
numbers = [1, 2, 3, 4, 5]
print("numbers:", numbers)

# 3. Mixed-type list
mixed = [1, "two", 3.0, True]
print("mixed:", mixed)

# 4. Repeated values
zeros = [4,10] * 5
print("zeros:", zeros)

# 5. Concatenation and repetition
a = [1, 2]
b = [3, 4]
concat = a + b
print("concat:", concat)
double = a * 2
print("double:", double)

# 6. Build with a loop (no def)
squares = []
for i in [1, 2, 3, 4, 5]:
    squares.append(i * i)
print(squares)

# 7. List comprehension
cubes = [i * i for i in range(1, 6)]
print("cubes (comprehension):", cubes)

# 8. Nested lists (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print("matrix row 2:", matrix[1])
print("matrix[2][1]:", matrix[2][1])  # 8

# 9. Copy via slicing and modify to show independence
copy_of_numbers = numbers[:]
copy_of_numbers[0] = 99
print("numbers:", numbers)
print("copy_of_numbers:", copy_of_numbers)

# 10. Unpacking into variables
first, second, *rest = numbers
print("first:", first, "second:", second, "rest:", rest)



