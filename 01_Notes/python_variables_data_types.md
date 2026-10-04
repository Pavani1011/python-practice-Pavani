# Python – Variables and Data Types

## 1. What Is a Variable?

**Definition:**

A variable is a name used to store a value in a program.

Think of a variable as a box with a label. The label is the variable name, and the value is what the box holds.

### Real-life example

Imagine:
- A box named `name` stores "Pavani".
- A box named `age` stores `26`.
- A box named `salary` stores `15000`.

In Python:

```python
name = "Pavani"
age = 26
salary = 15000

print(name)
print(age)
print(salary)
```

**Output:**

```text
Pavani
26
15000
```

### Explanation

- `name`, `age`, and `salary` are variable names.
- `=` is the assignment operator.
- `"Pavani"`, `26`, and `15000` are values.
- `print()` displays the values.

**Important:** In Python, `=` assigns a value. It does not mean "equal to" in the mathematical sense.

---

## 2. How to Create Variables

Python does not require you to declare a variable's type before assigning a value.

### Example 1: Store a string

```python
city = "Hyderabad"
print(city)
```

Output:

```text
Hyderabad
```

### Example 2: Store an integer

```python
marks = 95
print(marks)
```

Output:

```text
95
```

### Example 3: Store a decimal number

```python
price = 99.50
print(price)
```

Output:

```text
99.5
```

### Example 4: Change a variable's value

```python
score = 10
print(score)

score = 20
print(score)
```

Output:

```text
10
20
```

The variable `score` first stores `10`. Later, its value is replaced with `20`.

---

## 3. Rules for Naming Variables

Follow these rules when creating variable names:

1. A variable name can contain letters, numbers and underscores.
2. It cannot start with a number.
3. It cannot contain spaces.
4. Variable names are case-sensitive.
5. Python keywords cannot be used as variable names.

### Valid variable names

```python
name = "Pavani"
age = 26
total_marks = 450
employee1 = "Ravi"
```

### Invalid variable names

```python
# Invalid: starts with a number
1name = "Pavani"

# Invalid: contains a space
first name = "Pavani"

# Invalid: Python keyword
class = "Python"
```

The invalid examples above are intentionally shown as comments so the whole program can still run.

### Case-sensitive example

```python
age = 26
Age = 30

print(age)
print(Age)
```

Output:

```text
26
30
```

Python treats `age` and `Age` as two different variables.

### Best practice

Use meaningful variable names.

Good:

```python
customer_name = "Pavani"
account_balance = 5000
```

Avoid unclear names:

```python
x = "Pavani"
y = 5000
```

---

## 4. What Are Data Types?

**Definition:**

A data type tells Python what kind of value a variable contains.

For example:
- A name is text.
- An age is a whole number.
- A price can contain a decimal value.
- A yes/no answer can be represented by `True` or `False`.

### Common Python data types

| Data type | Description | Example |
|---|---|---|
| `int` | Whole numbers | `25` |
| `float` | Decimal numbers | `25.5` |
| `str` | Text | `"Hello"` |
| `bool` | True or false values | `True` |
| `list` | Ordered, changeable collection | `[10, 20, 30]` |
| `tuple` | Ordered, unchangeable collection | `(10, 20, 30)` |
| `set` | Collection of unique values | `{10, 20, 30}` |
| `dict` | Key-value pairs | `{"name": "Pavani"}` |

---

## 5. Numeric Data Types

### A. Integer (`int`)

An integer is a whole number without a decimal point.

```python
age = 26
quantity = 100
temperature = -5

print(age)
print(quantity)
print(temperature)
```

Output:

```text
26
100
-5
```

### B. Float (`float`)

A float is a number that has a decimal point.

```python
height = 162.5
price = 99.99
percentage = 85.5

print(height)
print(price)
print(percentage)
```

Output:

```text
162.5
99.99
85.5
```

### Difference between int and float

```python
a = 10
b = 10.5

print(type(a))
print(type(b))
```

Output:

```text
<class 'int'>
<class 'float'>
```

---

## 6. String (`str`)

A string is a sequence of characters used to represent text.

Strings can be written using single or double quotation marks.

```python
name = "Pavani"
city = 'Hyderabad'

print(name)
print(city)
```

Output:

```text
Pavani
Hyderabad
```

### String with spaces

```python
message = "Welcome to Python"
print(message)
```

Output:

```text
Welcome to Python
```

### Joining strings

```python
first_name = "Pavani"
last_name = "Dumpala"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Pavani Dumpala
```

The `+` operator joins strings together. This is called string concatenation.

---

## 7. Boolean (`bool`)

A Boolean represents one of two values: `True` or `False`.

```python
is_python_easy = True
is_exam_completed = False

print(is_python_easy)
print(is_exam_completed)
```

Output:

```text
True
False
```

### Boolean with a condition

```python
age = 26

print(age > 18)
```

Output:

```text
True
```

Python checks whether `age` is greater than `18`. Since the condition is true, the result is `True`.

---

## 8. List (`list`)

A list stores multiple values in a single variable.

Lists are:
- Ordered
- Changeable
- Able to contain duplicate values

```python
fruits = ["apple", "banana", "orange"]

print(fruits)
print(fruits[0])
print(fruits[1])
```

Output:

```text
['apple', 'banana', 'orange']
apple
banana
```

**Important:** Python indexing starts at `0`.

- `fruits[0]` gives the first item.
- `fruits[1]` gives the second item.
- `fruits[2]` gives the third item.

### Change a list value

```python
fruits = ["apple", "banana", "orange"]

fruits[1] = "mango"

print(fruits)
```

Output:

```text
['apple', 'mango', 'orange']
```

---

## 9. Tuple (`tuple`)

A tuple also stores multiple values in a single variable.

Unlike a list, a tuple cannot be changed after it is created.

```python
colors = ("red", "green", "blue")

print(colors)
print(colors[0])
```

Output:

```text
('red', 'green', 'blue')
red
```

### List vs tuple

| List | Tuple |
|---|---|
| Uses square brackets `[]` | Uses parentheses `()` |
| Changeable | Unchangeable |
| Example: `[1, 2, 3]` | Example: `(1, 2, 3)` |

---

## 10. Set (`set`)

A set stores unique values. Duplicate values are removed.

```python
numbers = {10, 20, 20, 30}

print(numbers)
```

Example output:

```text
{10, 20, 30}
```

The order of elements in a set is not guaranteed.

### Important points

- Sets do not allow duplicate elements.
- Sets are changeable.
- Sets do not support accessing items by index.

---

## 11. Dictionary (`dict`)

A dictionary stores information as key-value pairs.

Think of a customer record:
- `name` is a key.
- `"Pavani"` is its value.
- `age` is another key.
- `26` is its value.

```python
customer = {
    "name": "Pavani",
    "age": 26,
    "city": "Hyderabad"
}

print(customer)
print(customer["name"])
print(customer["age"])
```

Output:

```text
{'name': 'Pavani', 'age': 26, 'city': 'Hyderabad'}
Pavani
26
```

### Change a dictionary value

```python
customer = {
    "name": "Pavani",
    "age": 26
}

customer["age"] = 27

print(customer)
```

Output:

```text
{'name': 'Pavani', 'age': 27}
```

---

## 12. How to Check a Variable's Data Type

Python provides the built-in `type()` function to check a value's data type.

```python
name = "Pavani"
age = 26
height = 162.5
is_working = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_working))
```

Output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

---

## 13. Type Conversion

**Definition:**

Type conversion means changing a value from one data type to another.

Python provides functions such as:
- `int()` – converts a compatible value to an integer.
- `float()` – converts a compatible value to a float.
- `str()` – converts a value to a string.
- `bool()` – converts a value to a Boolean.

### Example 1: String to integer

```python
age = "26"

age = int(age)

print(age)
print(type(age))
```

Output:

```text
26
<class 'int'>
```

### Example 2: Integer to float

```python
number = 10

number = float(number)

print(number)
print(type(number))
```

Output:

```text
10.0
<class 'float'>
```

### Example 3: Integer to string

```python
number = 100

number = str(number)

print(number)
print(type(number))
```

Output:

```text
100
<class 'str'>
```

### Important warning

Not every value can be converted to every type.

For example:

```python
number = int("hello")
```

This causes a `ValueError` because `"hello"` is not a valid integer.

---

## 14. Combining Variables and Data Types

### Example: Employee details

```python
employee_name = "Pavani"
employee_id = 101
salary = 15000.50
is_active = True

print("Employee:", employee_name)
print("ID:", employee_id)
print("Salary:", salary)
print("Active:", is_active)
```

Output:

```text
Employee: Pavani
ID: 101
Salary: 15000.5
Active: True
```

### Example: Calculate total price

```python
price = 250
quantity = 4

total = price * quantity

print("Total price:", total)
```

Output:

```text
Total price: 1000
```

---

## 15. Interview Questions

**Q1. What is a variable in Python?**

A variable is a name used to store a value in a program.

**Q2. Do we need to declare variable types in Python?**

No. Python determines the type from the assigned value.

**Q3. What are the common built-in data types in Python?**

Common types include `int`, `float`, `str`, `bool`, `list`, `tuple`, `set` and `dict`.

**Q4. What is the difference between `int` and `float`?**

`int` represents whole numbers, while `float` represents numbers with decimal points.

**Q5. What is the difference between a list and a tuple?**

A list is changeable, while a tuple is unchangeable after creation.

**Q6. What is a dictionary?**

A dictionary stores data as key-value pairs.

**Q7. What is type conversion?**

Type conversion is changing a value from one data type to another.

**Q8. What is the purpose of the `type()` function?**

It returns the type of an object.

**Q9. What does case-sensitive mean in Python?**

It means uppercase and lowercase letters are treated differently. For example, `age` and `Age` are different variable names.

**Q10. What happens if we try to convert `"hello"` to an integer?**

Python raises a `ValueError` because the text is not a valid integer.

---

## 16. Practice Programs

Try these programs yourself before checking the examples above.

### Practice 1: Personal details

Create variables for your name, age, city and profession. Print all four values.

### Practice 2: Basic calculation

Create two number variables. Print their:
- Sum
- Difference
- Product
- Division result

### Practice 3: Data types

Create one variable each for a string, integer, float, Boolean, list and dictionary. Print the type of each variable using `type()`.

### Practice 4: Type conversion

Store `"100"` in a variable. Convert it to an integer, add `50`, and print the result.

### Practice 5: Employee salary

Create variables for an employee's name, monthly salary and number of months. Calculate and print the total salary for those months.

---

## 17. Quick Revision

- **Variable:** A named place to store a value.
- **Data type:** Describes the kind of value.
- **`int`:** Whole number.
- **`float`:** Decimal number.
- **`str`:** Text.
- **`bool`:** `True` or `False`.
- **`list`:** Ordered, changeable collection.
- **`tuple`:** Ordered, unchangeable collection.
- **`set`:** Collection of unique values.
- **`dict`:** Key-value collection.
- **`type()`:** Checks a value's type.
- **Type conversion:** Changes a value's data type.

