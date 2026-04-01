#Python Operators

#Arithmetic Operators

a = 10
b = 3

print(a + b)   # Addition → 13
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 30
print(a / b)   # Division → 3.333...
print(a // b)  # Floor Division → 3
print(a % b)   # Modulus → 1
print(a ** b)  # Exponentiation → 1000
#Used for mathematical computations.

#Assignment Operators

x = 10
x += 5   # x = x + 5
x -= 2   # x = x - 2
x *= 3   # x = x * 3
x /= 2   # x = x / 2

print(x)  # Output: 19.5
#Short-hand syntax for updating variable values.

#Comparison (Relational) Operators
a = 5
b = 10

print(a == b)   # Equal to → False
print(a != b)   # Not equal → True
print(a > b)    # Greater than → False
print(a < b)    # Less than → True
print(a >= b)   # Greater than or equal → False
print(a <= b)   # Less than or equal → True
#Return boolean results (True / False).

#Logical Operators

x = 5
y = 10

print(x > 2 and y > 5)   # True
print(x > 8 or y > 5)    # True
print(not(x > 2))        # False
#Combine conditional expressions.

#Bitwise Operators
a = 10  # 1010 in binary
b = 4   # 0100 in binary

print(a & b)   # AND → 0
print(a | b)   # OR → 14
print(a ^ b)   # XOR → 14
print(~a)      # NOT → -11
print(a << 1)  # Left shift → 20
print(a >> 1)  # Right shift → 5
#Operate at the binary level.

# Membership Operators
fruits = ["apple", "banana", "orange"]

print("apple" in fruits)      # True
print("grape" not in fruits)  # True
#Test whether a value exists in a sequence.

# Identity Operators

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True (same object)
print(a is c)      # False (different objects)
print(a == c)      # True (values equal)
#Check memory identity, not equality.

#Unary Operators
x = 5

print(+x)  # Unary plus → 5
print(-x)  # Unary minus → -5
#Operate on a single operand.

#Ternary (Conditional) Operator
age = 20

status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult
#Compact conditional assignment syntax.

#10. Operator Precedence
result = 10 + 5 * 2 ** 2
print(result)  # Output: 30
