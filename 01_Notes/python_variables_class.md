
# 1. Creating variables
name = "Pavani"
age = 26
height = 5.11
is_learning = True

print(name)
print(age)
print(height)
print(is_learning)


# 2. Checking data types
print(type(name))          # str
print(type(age))           # int
print(type(height))        # float
print(type(is_learning))   # bool


# 3. Dynamic type inference
weight = 99
print(type(weight))        # int


# 4. Dynamic typing
weight = 99
print(type(weight))        # int

weight = weight + 0.350
print(weight)
print(type(weight))        # float

weight = "99 kg"
print(type(weight))        # str


# 5. Strong typing
name = "Pavani"
weight = 99

# print(name + weight)     # TypeError

print(name + str(weight))  # Pavani99


# 6. Combining values
print(name, weight)
print(f"My name is {name}, weight is {weight}")


# 7. Variable reassignment
number = 100
print(number)

number = 200
print(number)

number = "Python"
print(number)


# 8. Variable naming
student_name = "Pavani"
_age = 26
height1 = 5.11

print(student_name)
print(_age)
print(height1)

# Invalid variable names:
# 1name = "Pavani"
# student-name = "Pavani"
# class = "Python"


# 9. Case sensitivity
name = "Inceptez Technologies"
Name = "Inceptez!"
NAME = "INCEPTEZ"

print(name)
print(Name)
print(NAME)


# 10. Naming conventions
student_name = "Pavani"   # Snake case
studentName = "Pavani"    # Camel case


# 11. Type conversion
age = 26
age_text = str(age)
print(age_text, type(age_text))

price_text = "250"
price = int(price_text)
print(price, type(price))

height_text = "5.11"
height = float(height_text)
print(height, type(height))


# 12. Real-life salary calculation
monthly_salary = 15000
annual_salary = monthly_salary * 12

print("Monthly salary:", monthly_salary)
print("Annual salary:", annual_salary)


# 13. Multiple assignment
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)


# 14. Same value assigned to multiple variables
a = b = c = 100

print(a)
print(b)
print(c)


# 15. Checking a data type
value = 100

if isinstance(value, int):
    print("Value is an integer")
else:
    print("Value is not an integer")


# 16. Real-life shopping bill
product_name = "Lipstick"
price = 250
quantity = 2

total = price * quantity

print("Product:", product_name)
print("Price:", price)
print("Quantity:", quantity)
print("Total:", total)
