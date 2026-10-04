# Python Practice – Operators

## 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

```python
a = 20
b = 10

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
```

**Expected output:**
Addition: 30
Subtraction: 10
Multiplication: 200
Division: 2.0
Floor Division: 2
Modulus: 0
Exponent: 1024
```

## 2. Arithmetic with Different Numbers

```python
a = 17
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

**Expected output:**

22
12
85
3.4
3
2
1419857
```

## 3. Comparison Operators

Comparison operators compare two values and return `True` or `False`.

```python
a = 20
b = 10

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

**Expected output:**

False
True
True
False
True
False
```

## 4. Logical Operators

Logical operators combine or reverse conditions.

```python
age = 26
salary = 15000

print(age > 18 and salary > 10000)
print(age > 30 or salary > 10000)
print(not(age > 18))
```

**Expected output:**

True
True
False
```

## 5. Assignment Operators

Assignment operators assign or update variable values.

```python
number = 10

number += 5
print(number)

number -= 3
print(number)

number *= 2
print(number)

number /= 4
print(number)
```

**Expected output:**
15
12
24
6.0
```

## 6. Membership Operators

Membership operators check whether a value exists in a collection.

```python
fruits = ["apple", "banana", "orange"]

print("apple" in fruits)
print("mango" in fruits)
print("mango" not in fruits)
```

**Expected output:**
True
False
True
```

## 7. Identity Operators

Identity operators check whether two variables refer to the same object.

```python
a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b)
print(a is c)
print(a == c)
print(a is not c)
```

**Expected output:**
True
False
True
True
```

Remember:
- `is` checks object identity.
- `==` checks value equality.

## 8. Real-Life Calculation – Shopping Bill

```python
item_price = 250
quantity = 4
discount = 100

total = item_price * quantity
final_amount = total - discount

print("Total:", total)
print("Discount:", discount)
print("Final amount:", final_amount)
```

**Expected output:**
Total: 1000
Discount: 100
Final amount: 900
```

## 9. Real-Life Calculation – Employee Salary

```python
basic_salary = 25000
bonus = 5000
deduction = 2000

total_salary = basic_salary + bonus - deduction

print("Final salary:", total_salary)
```

**Expected output:**
Final salary: 28000
```

## 10. Practice Challenges

Try solving these without copying the examples.

**Challenge 1: Simple Calculator**

Create two number variables and print their sum, difference, product and division.

**Challenge 2: Even or Odd**

Use the modulus operator to check whether a number is even or odd. For example, test `24` and `17`.

**Challenge 3: Age Comparison**

Create an age variable and check whether the person is:
- Older than 18
- Exactly 18
- Younger than 18

**Challenge 4: Eligibility Check**

Create variables for age and exam score. Check whether age is at least 18 and score is at least 50 using `and`.

**Challenge 5: Shopping Discount**

Create variables for product price, quantity and discount. Calculate the final bill.

---

## Quick Revision

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `//` | Floor division | `11 // 5` |
| `%` | Remainder | `11 % 5` |
| `**` | Exponent | `2 ** 3` |
| `==` | Equal to | `10 == 10` |
| `!=` | Not equal to | `10 != 5` |
| `>` | Greater than | `10 > 5` |
| `<` | Less than | `5 < 10` |
| `and` | Both conditions true | `True and True` |
| `or` | At least one condition true | `True or False` |
| `not` | Reverses a Boolean | `not True` |
| `in` | Membership check | `"a" in "cat"` |
| `is` | Object identity | `a is b` |
