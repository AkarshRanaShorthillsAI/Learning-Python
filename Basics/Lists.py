# 1. Declaring a List
my_list = [1, 2, 3, "hello", 4.5]

# 2. Accessing Elements in a List
# a) Positive Indexing
print("Accessing elements using positive indexing:")
my_list = [10, 20, 30, 40, 50]
print(my_list[0])  # Output: 10
print(my_list[2])  # Output: 30

# b) Negative Indexing
print("Accessing elements using negative indexing:")
print(my_list[-1])  # Output: 50
print(my_list[-3])  # Output: 30

# 3. Looping Through a List
# a) Using a for Loop
print("Looping through a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# b) Using if Statements in a Loop
print("Using if statements in a loop:")
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        print(f"Even number: {num}")

# 4. List Methods
# a) append()
print("Using append method:")
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# b) remove()
print("Using remove method:")
my_list = ["a", "b", "c", "b"]
my_list.remove("b")
print(my_list)  # Output: ["a", "c", "b"]

# c) insert()
print("Using insert method:")
my_list = [1, 2, 4]
my_list.insert(2, 3)  # Inserts 3 at index 2
print(my_list)  # Output: [1, 2, 3, 4]

# d) copy()
print("Using copy method:")
original_list = [1, 2, 3]
copied_list = original_list.copy()
print(copied_list)  # Output: [1, 2, 3]

# 5. List Comprehension
print("Using list comprehension:")
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
