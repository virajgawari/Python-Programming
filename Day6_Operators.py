# 06-JAN-2026

# Practicing different types of operators with simple examples

# Arithmetic Operators

a = 10
b = 3

print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Exponent:", a ** b)

print("\n----------------------------")


# Comparison Operators

x = 10
y = 5

print("Comparison Operators")
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

print("\n----------------------------")


# Logical Operators

age = 18

print("Logical Operators")
print("age > 10 and age < 30:", age > 10 and age < 30)
print("age > 20 or age == 18:", age > 20 or age == 18)
print("not(age == 18):", not(age == 18))

print("\n----------------------------")


# Assignment Operators

num = 5
print("Assignment Operators")

num += 2
print("After += 2:", num)

num *= 3
print("After *= 3:", num)

print("\n----------------------------")


# Membership Operators

numbers = [1, 2, 3, 4, 5]

print("Membership Operators")
print("3 in numbers:", 3 in numbers)
print("10 not in numbers:", 10 not in numbers)

print("\n----------------------------")


# Identity Operators

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("Identity Operators")
print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 == list3:", list1 == list3)

print("\n----------------------------")


# Bitwise Operators

a = 5   # binary: 101
b = 3   # binary: 011

print("Bitwise Operators")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
