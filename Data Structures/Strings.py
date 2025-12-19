# 1. String creation
s1 = "Hello, World!"
s2 = 'Single quotes work too'
s3 = str(123)
print(s1, s2, s3, sep="\n")

print(s1)
print(s2)
print(s3)


print("--------------")

# 2. String indexing and slicing
s = "Hello, World"
print(s[1])        # First character
print(s[-1])       # Last character
print(s[0:5])     # First five characters
print(s[7:])      # From index 7 to end
print(s[:5])      # From start to index 5


print("--------------")
# 3. String methods
s = "hello world  "
print(s.upper())          # Convert to uppercase
print(s.capitalize())     # Capitalize first letter
print(s.replace("world", "there"))  # Replace substring
print(s.split(" "))       # Split string into list
print(s.find("world"))    # Find substring index
print(len(s))             # Length of string
print(s.strip())          # Remove whitespace from ends
print(s.startswith("hello"))  # Check start
print(s.endswith("world"))    # Check end
print(s.count("o"))       # Count occurrences
print(s.isalpha())       # Check if all characters are alphabetic
print(s.isdigit())       # Check if all characters are digits
print(s.join(["lolo", "dodo"]))  # Join list into string
print(s.index("world"))   # Get index of substring
print(s.lower())          # Convert to lowercase
print(s.title())          # Title case
print(s.zfill(50))       # Pad string with zeros to length 50
print(s.center(50))      # Center string in a field of width 50



print("--------------")



# 4. String formatting
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")
print("My name is {0} and I am {1} years old.".format(name, age))
print("My name is {sahu} and I am {shubh} years old.".format(sahu=name, shubh=age))



print("--------------")

# 5. Multiline strings

multi_line = """This is a
multiline string. It can span multiple lines.
You can include line breaks and indentation.
Enjoy working with strings!"""
print(multi_line)


print("--------------")

# 6. Immutable nature of strings
s = 100
try:
    s[0] = "I"
except TypeError:
    print(TypeError("dekh na love , check again"))
print(s)