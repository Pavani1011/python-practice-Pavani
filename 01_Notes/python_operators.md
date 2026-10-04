# Python – Operators

## 1. What Are Operators?

**Definition:**

Operators are special symbols or keywords used to perform operations on variables and values.

### Real-life example

Suppose you buy 3 notebooks, and each notebook costs ₹50.

- Price = ₹50
- Quantity = 3
- Total cost = ₹50 × 3 = ₹150

In Python:

```python
price = 50
quantity = 3

total = price * quantity

print(total)
```

**Output:**

```text
150
```

Here, `*` is an arithmetic operator used for multiplication.

---

## 2. Types of Python Operators

Python has several categories of operators:

1. Arithmetic operators
2. Comparison operators
3. Logical operators
4. Assignment operators
5. Membership operators
6. Identity operators
7. Bitwise operators

---

## 3. Arithmetic Operators

**Definition:**

Arithmetic operators are used to perform mathematical calculations.

| Operator | Name | Description | Example | Result |
|---|---|---|---|---|
| `+` | Addition | Adds two values | `10 + 5` | `15` |
| `-` | Subtraction | Subtracts one value from another | `10 - 5` | `5` |
| `*` | Multiplication | Multiplies two values | `10 * 5` | `50` |
| `/` | Division | Divides one value by another | `10 / 5` | `2.0` |
| `//` | Floor division | Gives the quotient rounded down | `11 // 5` | `2` |
| `%` | Modulus | Gives the remainder | `11 % 5` | `1` |
| `**` | Exponentiation | Raises a number to a power | `2 ** 3` | `8` |

### Important concepts

**Division (`/`)**

Returns a floating-point result for ordinary numeric division.

Example:

```python
print(10 / 2)
```

Output:

```text
5.0
```

**Floor division (`//`)**

Divides and rounds the result down to the nearest whole number.

Example:

```python
print(11 // 5)
```

Output:

```text
2
```

**Modulus (`%`)**

Returns the remainder after division.

Example:

```python
print(11 % 5)
```

Output:

```text
1
```

**Exponentiation (`**`)**

Calculates a number raised to a power.

Example:

```python
print(2 ** 3)
```

Output:

```text
8
```

---

## 4. Comparison Operators

**Definition:**

Comparison operators compare two values and return a Boolean result: `True` or `False`.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `10 == 10` | `True` |
| `!=` | Not equal to | `10 != 5` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<` | Less than | `5 < 10` | `True` |
| `>=` | Greater than or equal to | `10 >= 10` | `True` |
| `<=` | Less than or equal to | `5 <= 10` | `True` |

### Example

```python
a = 20
b = 10

print(a == b)
print(a != b)
print(a > b)
print(a < b)
```

Output:

```text
False
True
True
False
```

### Important difference

- `=` assigns a value to a variable.
- `==` compares two values to check whether they are equal.

---

## 5. Logical Operators

**Definition:**

Logical operators combine conditions or reverse a condition's Boolean result.

Python has three logical operators.

| Operator | Description |
|---|---|
| `and` | Returns `True` when both conditions are true |
| `or` | Returns `True` when at least one condition is true |
| `not` | Reverses the Boolean result |

### A. AND operator

Both conditions must be true.

```python
age = 26
salary = 15000

print(age > 18 and salary > 10000)
```

Output:

```text
True
```

### B. OR operator

At least one condition must be true.

```python
age = 17
salary = 15000

print(age > 18 or salary > 10000)
```

Output:

```text
True
```

### C. NOT operator

Reverses the Boolean result.

```python
is_learning = True

print(not is_learning)
```

Output:

```text
False
```

### Truth table

| A | B | A and B | A or B |
|---|---|---|---|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

---

## 6. Assignment Operators

**Definition:**

Assignment operators assign values to variables or update their existing values.

| Operator | Example | Equivalent expression |
|---|---|---|
| `=` | `a = 10` | Assigns `10` to `a` |
| `+=` | `a += 5` | `a = a + 5` |
| `-=` | `a -= 5` | `a = a - 5` |
| `*=` | `a *= 5` | `a = a * 5` |
| `/=` | `a /= 5` | `a = a / 5` |
| `//=` | `a //= 5` | `a = a // 5` |
| `%=` | `a %= 5` | `a = a % 5` |
| `**=` | `a **= 2` | `a = a ** 2` |

### Example

```python
number = 10

number += 5
print(number)

number *= 2
print(number)

number -= 4
print(number)
```

Output:

```text
15
30
26
```

---

## 7. Membership Operators

**Definition:**

Membership operators check whether a value exists in a sequence or collection.

Python provides two membership operators:

- `in`
- `not in`

### Example

```python
fruits = ["apple", "banana", "orange"]

print("apple" in fruits)
print("mango" in fruits)
print("mango" not in fruits)
```

Output:

```text
True
False
True
```

### Explanation

- `"apple" in fruits` checks whether apple exists in the list.
- `"mango" in fruits` checks whether mango exists.
- `"mango" not in fruits` checks whether mango is absent.

---

## 8. Identity Operators

**Definition:**

Identity operators check whether two variables refer to the same object in memory.

Python provides two identity operators:

- `is`
- `is not`

### Example

```python
a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b)
print(a is c)
print(a == c)
print(a is not c)
```

Output:

```text
True
False
True
True
```

### Explanation

- `a is b` is `True` because both refer to the same list object.
- `a is c` is `False` because `c` is a separate list object.
- `a == c` is `True` because both lists contain equal values.
- `a is not c` is `True` because they are different objects.

### Difference between `is` and `==`

| `is` | `==` |
|---|---|
| Checks object identity | Checks value equality |
| Checks whether two references point to the same object | Checks whether values are equal |
| Example: `a is b` | Example: `a == b` |

Use `==` when comparing values. Use `is` when checking object identity, such as `value is None`.

---

## 9. Bitwise Operators

**Definition:**

Bitwise operators perform operations on the binary representations of integers.

| Operator | Name | Description |
|---|---|---|
| `&` | AND | Sets a bit if both corresponding bits are 1 |
| `\|` | OR | Sets a bit if at least one corresponding bit is 1 |
| `^` | XOR | Sets a bit if corresponding bits are different |
| `~` | NOT | Inverts the bits |
| `<<` | Left shift | Shifts bits to the left |
| `>>` | Right shift | Shifts bits to the right |

### Example

```python
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(a << 1)
print(a >> 1)
```

Output:

```text
1
7
6
10
2
```

Bitwise operations are useful in certain low-level programming tasks, flags and performance-sensitive operations.

---

## 10. Operator Precedence

**Definition:**

Operator precedence determines the order in which Python evaluates operators in an expression.

### Example

```python
result = 10 + 5 * 2

print(result)
```

Output:

```text
20
```

Multiplication is evaluated before addition.

### Using parentheses

```python
result = (10 + 5) * 2

print(result)
```

Output:

```text
30
```

Parentheses change the order of evaluation.

### Basic precedence order

From higher to lower precedence:

1. Parentheses: `()`
2. Exponentiation: `**`
3. Multiplication, division, floor division and modulus: `*`, `/`, `//`, `%`
4. Addition and subtraction: `+`, `-`
5. Comparison operators
6. Logical `not`
7. Logical `and`
8. Logical `or`

When in doubt, use parentheses to make expressions easier to read.

---

## 11. Real-Life Applications

### Shopping bill

```python
price = 250
quantity = 4
discount = 100

total = price * quantity
final_amount = total - discount

print("Total:", total)
print("Discount:", discount)
print("Final amount:", final_amount)
```

Output:

```text
Total: 1000
Discount: 100
Final amount: 900
```

### Employee salary

```python
basic_salary = 25000
bonus = 5000
deduction = 2000

total_salary = basic_salary + bonus - deduction

print("Final salary:", total_salary)
```

Output:

```text
Final salary: 28000
```

### Checking eligibility

```python
age = 25
exam_score = 75

eligible = age >= 18 and exam_score >= 50

print(eligible)
```

Output:

```text
True
```

---

## 12. Interview Questions

**Q1. What are operators in Python?**

Operators are symbols or keywords used to perform operations on values and variables.

**Q2. What is the difference between `/` and `//`?**

`/` performs division and returns a floating-point result. `//` performs floor division and rounds the result down.

**Q3. What does the modulus operator do?**

The `%` operator returns the remainder after division.

**Q4. What is the difference between `=` and `==`?**

`=` assigns a value, while `==` compares two values for equality.

**Q5. What is the difference between `and` and `or`?**

`and` requires both conditions to be true. `or` requires at least one condition to be true.

**Q6. What are membership operators?**

`in` and `not in` check whether a value exists in a collection or sequence.

**Q7. What is the difference between `is` and `==`?**

`is` checks object identity, while `==` checks value equality.

**Q8. What is operator precedence?**

Operator precedence defines the order in which operators are evaluated in an expression.

**Q9. What are assignment operators?**

Assignment operators assign or update values in variables, such as `=`, `+=` and `-=`.

**Q10. What are bitwise operators?**

Bitwise operators perform operations on the binary representation of integers.

---

## 13. Quick Revision

- **Arithmetic:** Mathematical calculations.
- **Comparison:** Compares values and returns Boolean results.
- **Logical:** Combines or reverses conditions.
- **Assignment:** Assigns or updates variable values.
- **Membership:** Checks whether a value exists in a collection.
- **Identity:** Checks whether two references point to the same object.
- **Bitwise:** Performs operations on binary representations.
- **Precedence:** Determines the evaluation order of operators.
