# Creating dictionaries
empty_dict = {}
print("empty_dict:", empty_dict)
# 2. Literal dictionary with key-value pairs

person = {"name": "Alice", "age": 30, "city": "New York"}

print("person:", person)

# 3. Using dict() constructor

data = dict(country="USA", language="English")

print("data:", data)

print("-----------------------------")
# 4. Accessing values by keys
print("person name:", person["name"])
print("data language:", data.get("language"))

print("-----------------------------")
# 5. Adding and updating key-value pairs
person["profession"] = "Engineer"
print("updated person:", person)

print("-----------------------------")
data["currency"] = "USD"
print("updated data:", data)

print("-----------------------------")

# 6. Removing key-value pairs
removed_value = person.pop("age")
print("removed age:", removed_value)

print("person after removal:", person)

print("-----------------------------")


del data["language"]
print("data after deletion:", data) 

print("-----------------------------")


# 7. Dictionary methods
keys = person.keys()
values = person.values()
items = person.items()
print("person keys:", keys)
print("person values:", values)
print("person items:", items)

print("-----------------------------")

# 8. Iterating through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")

print("-----------------------------")




# outputs are 
# empty_dict: {}
# person: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# data: {'country': 'USA', 'language': 'English'}
# -----------------------------
# person name: Alice
# data language: English
# -----------------------------
# updated person: {'name': 'Alice', 'age': 30, 'city': 'New York', 'profession': 'Engineer'}
# -----------------------------
# updated data: {'country': 'USA', 'language': 'English', 'currency': 'USD'}
# -----------------------------
# removed age: 30
# person after removal: {'name': 'Alice', 'city': 'New York', 'profession': 'Engineer'}
# -----------------------------
# data after deletion: {'country': 'USA', 'currency': 'USD'}
# -----------------------------
# person keys: dict_keys(['name', 'city', 'profession'])
# person values: dict_values(['Alice', 'New York', 'Engineer'])
# person items: dict_items([('name', 'Alice'), ('city', 'New York'), ('profession', 'Engineer')])
# -----------------------------
# name: Alice
# city: New York
# profession: Engineer
# -----------------------------

