# 1) Defining & calling (positional)
def greet(name):
    print("My name is {name}".format(name=name))

greet("Shubh")
greet(10)

print('-------------------------')
# 2) Default argument
def power(base, exponent=2):
    return base ** exponent

print(power(3))
print(power(2, 5))
print(power(base=5, exponent=3))


print('-------------------------')

# 3) Variable length positional arguments (*args)
def summarize(*args):
    print("Items:", args)
    return sum(args)

print(summarize(1,2,3,4,5))

def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(add_all(1,2,3,4,5))

print('-----------------------')


# 6) Return statement and multiple return values (tuple unpacking)
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder


q, r = divide(105, 10)
print(q,r)

print('-----------------------')