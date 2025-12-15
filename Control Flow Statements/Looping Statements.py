# loop

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# For loop with range
for i in range(15,-20,-2):
    print(i)



# while loop

count = 0
while count < 5:
    print(count)
    count += 1


# Nested loops example
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")


# loop break example
for num in range(10):
    if num == 5:
        break
    print(num)

# loop continue example
for num in range(20):
    if num % 3 == 0:
        continue
    print(num)

# loop pass example
for num in range(20):
    if num == 13:
        pass
    else:
        print(num)