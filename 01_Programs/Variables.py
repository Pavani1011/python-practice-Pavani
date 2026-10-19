
# ==========================================
# Python Variables and Data Types - Practice
# ==========================================

# Example 1: Creating variables
name = "Pavani"
age = 26
height = 162.5
is_learning_python = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Learning Python:", is_learning_python)


# Example 2: Checking data types
print(type(name))
print(type(age))
print(type(height))
print(type(is_learning_python))


# Example 3: Dynamic type inference
number = 100
print(number)
print(type(number))

price = 99.5
print(price)
print(type(price))


# Example 4: Dynamic typing
value = 100
print(value, type(value))

value = "Python"
print(value, type(value))

value = True
print(value, type(value))


# Example 5: Strong typing
number = 100
word = "Python"

# print(number + word)  # TypeError
print(str(number) + word)


# Example 6: Reassigning variables
salary = 600000
print("Old salary:", salary)

salary = 1200000
print("New salary:", salary)


# Example 7: Valid variable names
student_name = "Pavani"
_age = 26
marks1 = 90

print(student_name, _age, marks1)


# Example 8: Case-sensitive variables
name = "Pavani"
Name = "Python"

print(name)
print(Name)


# Example 9: Type conversion
age = "26"
print(type(age))

age = int(age)
print(age)
print(type(age))


# Example 10: Multiple assignment
a, b, c = 10, 20, 30
print(a, b, c)


# Example 11: Assigning the same value
x = y = z = 50
print(x, y, z)


# Example 12: Checking a data type
age = 26
print(isinstance(age, int))
print(isinstance(age, str))


# Example 13: Basic shopping example
item = "Lipstick"
price = 500
quantity = 2

total = price * quantity

print("Item:", item)
print("Price:", price)
print("Quantity:", quantity)
print("Total:", total)
