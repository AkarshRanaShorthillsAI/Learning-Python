# Creating a String
s1 = 'Hello'
s2 = "World"

# Multi-line Strings
s3 = '''Multiline 
String'''

# Accessing Characters in Python String
s = "Python"
print(s[0])  # Output: P
print(s[-1]) # Output: n

# String Immutability
s = "Immutable"
# s[0] = 'i'  # This will raise a TypeError

# Deleting a String
s = "Delete me"
del s
# print(s)  # This will raise a NameError 

# Updating a String
s = "Python"
s = s + " Programming"
print(s)  # Output: Python Programming

# Common String Methods
s = "hello world"
print(s.upper())  # Output: HELLO WORLD
print(s.lower())  # Output: hello world
print(s.title())  # Output: Hello World
print(s.replace("world", "Python"))  # Output: hello Python

# Concatenating and Repeating Strings
s1 = "Hello "
s2 = "World"
print(s1 + s2)  # Output: Hello World
print(s1 * 3)   # Output: Hello Hello Hello

# Formatting Strings
name = "Akarsh"
age = 22
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Akarsh and I am 22 years old.

# String Slicing
s = "Programming"
print(s[0:4])  # Output: Prog
print(s[-5:])  # Output: ming

# String Membership Testing
s = "Python Programming"
print("Python" in s)  # Output: True
print("Java" not in s)  # Output: True

# String Iteration
s = "Python"
for char in s:
    print(char)

# String Length Calculation
s = "Hello World"
print(len(s))  # Output: 11

# String Comparison
print("apple" == "Apple")  # Output: False
print("banana" > "apple")  # Output: True 


