
# 1. Declaring a Dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}

# 2. Accessing Dictionary Elements
print("Accessing elements:")
print(my_dict["name"])  # Output: John
# print(my_dict["gender"])  # Uncommenting this will raise a KeyError

# 3. Using .get() Method
print("Using .get() method:")
print(my_dict.get("age"))  # Output: 30
print(my_dict.get("gender"))  # Output: None
print(my_dict.get("gender", "Not Specified"))  # Output: Not Specified

# 4. Looping Through Dictionaries
# 4.1 Looping Through Keys Only
print("Looping through keys:")
for key in my_dict:
    print(key)

# 4.2 Looping Through Keys and Values
print("Looping through keys and values:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 5. Inserting Elements into a Dictionary
my_dict["gender"] = "Male"
print("Dictionary after insertion:")
print(my_dict)

# 6. Removing Elements from a Dictionary
# 6.1 Using pop()
removed_value = my_dict.pop("age")
print("Removed value:", removed_value)  # Output: 30
print("Dictionary after pop:")
print(my_dict)

# 6.2 Using popitem()
last_item = my_dict.popitem()
print("Last removed item:", last_item)
print("Dictionary after popitem:")

last_item = my_dict.popitem()
print("Last removed item:", last_item)
print("Dictionary after popitem:")

print(my_dict)



