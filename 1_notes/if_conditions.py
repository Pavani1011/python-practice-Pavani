
# ==========================================
# PYTHON BASICS
# TOPIC: IF CONDITIONS AND INDENTATION
# ==========================================

# Example 1: All print statements inside the if block

box = "pen"

if box == "pen":
    print("I found a pen")
    print("I can write with it")
    print("The checking is completed")

# Output:
# I found a pen
# I can write with it
# The checking is completed


# ==========================================
# Example 2: One print inside, two outside
# ==========================================

box = "pen"

if box == "pen":
    print("I found a pen")

print("I can write with it")
print("The checking is completed")

# Output:
# I found a pen
# I can write with it
# The checking is completed


# ==========================================
# Example 3: Condition is false
# All print statements inside the if block
# ==========================================

box = "pen"

if box == "pencil":
    print("I found a pencil")
    print("I can write with it")
    print("The checking is completed")

# Output:
# No output


# ==========================================
# Example 4: Condition is false
# One print inside, two outside
# ==========================================

box = "pen"

if box == "pencil":
    print("I found a pencil")

print("I can write with it")
print("The checking is completed")

# Output:
# I can write with it
# The checking is completed


# ==========================================
# Example 5: All three prints inside the if
# A blank line does not end the if block
# ==========================================

box = "pencil"

if box == "pencil":
    print("I found a pencil")
    print("I can write with it")

    print("Okay")

# Output:
# I found a pencil
# I can write with it
# Okay


# ==========================================
# Example 6: Using a false condition
# All prints outside the if block
# ==========================================

box = "pen"

if box == "pencil":
    print("I found a pencil")

print("I can write with it")
print("Okay")

# Output:
# I can write with it
# Okay


# ==========================================
# Example 7: Using if and else
# ==========================================

box = "pen"

if box == "pencil":
    print("Pencil found")
else:
    print("Pencil not found")

# Output:
# Pencil not found


# ==========================================
# Example 8: Checking a number
# ==========================================

age = 26

if age >= 18:
    print("Eligible to vote")

# Output:
# Eligible to vote


# ==========================================
# IMPORTANT POINTS
# ==========================================

# 1. = is used to assign a value.
# 2. == is used to compare two values.
# 3. : indicates the beginning of a block.
# 4. Indentation identifies statements inside a block.
# 5. Statements outside the if block run independently.
# 6. Four spaces are the standard indentation.
# 7. A blank line does not end an if block.
