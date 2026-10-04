# Python Practice Programs – Introduction to Variables and Data Types

These programs cover the Python basics learned so far. Each program includes code and its expected output.

## 1. Print Statements and Comments

```python
# My first Python program

print("Hello, Pavani!")
print("I am learning Python")
print("My goal is to become a Data Engineer")
```

**Output:**
Hello, Pavani!
I am learning Python
My goal is to become a Data Engineer
```

## 2. Variables

```python
name = "Pavani"
age = 26
city = "Srikakulam"
salary = 15000.50

print(name)
print(age)
print(city)
print(salary)
```

**Output:**
Pavani
26
Srikakulam
15000.5
```

## 3. Changing Variable Values

```python
score = 10
print(score)

score = 20
print(score)

score = score + 5
print(score)
```

**Output:**
10
20
25
```

## 4. Variable Naming and Case Sensitivity

```python
first_name = "Pavani"
employee1 = "Ravi"

age = 26
Age = 30

print(first_name)
print(employee1)
print(age)
print(Age)
```

**Output:**
Pavani
Ravi
26
30
```

## 5. Integer and Float

```python
age = 26
height = 162.5
temperature = -5

print(age)
print(height)
print(temperature)

print(type(age))
print(type(height))
print(type(temperature))
```

**Output:**
26
162.5
-5
<class 'int'>
<class 'float'>
<class 'int'>
```

## 6. Strings and String Concatenation

```python
first_name = "Pavani"
last_name = "Dumpala"

full_name = first_name + " " + last_name

print(full_name)

message = "Welcome to Python"
print(message)
```

**Output:**
Pavani Dumpala
Welcome to Python
```

## 7. Boolean and Comparisons

```python
is_learning = True
is_exam_completed = False

age = 26

print(is_learning)
print(is_exam_completed)
print(age > 18)
print(age == 26)
print(age < 18)
```

**Output:**
True
False
True
True
False
```

## 8. Lists and Indexing

```python
fruits = ["apple", "banana", "orange"]

print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])

fruits[1] = "mango"
print(fruits)

fruits.append("grapes")
print(fruits)
```

**Output:**
['apple', 'banana', 'orange']
apple
banana
orange
['apple', 'mango', 'orange']
['apple', 'mango', 'orange', 'grapes']
```

## 9. Tuples

```python
colors = ("red", "green", "blue")

print(colors)
print(colors[0])
print(colors[1])
print(type(colors))
```

**Output:**
('red', 'green', 'blue')
red
green
<class 'tuple'>
```

## 10. Sets

```python
numbers = {10, 20, 20, 30, 40}

print(numbers)
print(type(numbers))

numbers.add(50)
print(numbers)

numbers.remove(20)
print(numbers)
```

**Example output:**
{10, 20, 30, 40}
<class 'set'>
{10, 20, 30, 40, 50}
{10, 30, 40, 50}
```

Note: Set elements may appear in a different order.

## 11. Dictionaries

```python
customer = {
    "name": "Pavani",
    "age": 26,
    "city": "Hyderabad"
}

print(customer)
print(customer["name"])
print(customer["age"])

customer["age"] = 27
customer["salary"] = 15000

print(customer)
```

**Output:**
{'name': 'Pavani', 'age': 26, 'city': 'Hyderabad'}
Pavani
26
{'name': 'Pavani', 'age': 27, 'city': 'Hyderabad', 'salary': 15000}
```

## 12. Checking Data Types

```python
name = "Pavani"
age = 26
height = 162.5
is_working = True
fruits = ["apple", "banana"]
colors = ("red", "blue")
numbers = {1, 2, 3}
customer = {"name": "Pavani"}

print(type(name))
print(type(age))
print(type(height))
print(type(is_working))
print(type(fruits))
print(type(colors))
print(type(numbers))
print(type(customer))
```

**Output:**
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'list'>
<class 'tuple'>
<class 'set'>
<class 'dict'>
```

## 13. Type Conversion

```python
# String to integer
age = "26"
age = int(age)

print(age)
print(type(age))

# Integer to float
number = 10
number = float(number)

print(number)

# Integer to string
salary = 15000
salary = str(salary)

print(salary)
print(type(salary))

# String to float
price = "99.50"
price = float(price)

print(price)
```

**Output:**
26
<class 'int'>
10.0
15000
<class 'str'>
99.5
```

## 14. Employee Details

```python
employee_name = "Pavani"
employee_id = 101
monthly_salary = 15000.50
is_active = True

print("Employee:", employee_name)
print("ID:", employee_id)
print("Salary:", monthly_salary)
print("Active:", is_active)
```

**Output:**
Employee: Pavani
ID: 101
Salary: 15000.5
Active: True
```

## 15. Basic Calculations

```python
a = 20
b = 10

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
```

**Output:**
Addition: 30
Subtraction: 10
Multiplication: 200
Division: 2.0
```

## 16. Practice Challenges

Try solving these independently.

**Challenge 1: Personal Details**

Create variables for your name, age, city and profession. Print all four details.

**Challenge 2: Shopping Bill**

Create variables for item price and quantity. Calculate and print the total bill.

**Challenge 3: Student Marks**

Create a list of five marks. Print the first mark, last mark and list data type.

**Challenge 4: Customer Record**

Create a dictionary with customer name, age and city. Update the city and print the dictionary.

**Challenge 5: Convert and Calculate**

Store `"100"` in a variable. Convert it to an integer, add `50`, and print the result.

---

## Quick Revision

| Concept | Program |
|---|---|
| Print | `print("Hello")` |
| Variable | `age = 26` |
| Integer | `number = 10` |
| Float | `price = 99.5` |
| String | `name = "Pavani"` |
| Boolean | `is_valid = True` |
| List | `numbers = [1, 2, 3]` |
| Tuple | `numbers = (1, 2, 3)` |
| Set | `numbers = {1, 2, 3}` |
| Dictionary | `person = {"name": "Pavani"}` |
| Check type | `type(age)` |
| Convert to integer | `int("100")` |
