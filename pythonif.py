# 1 -Basic if statement

age = 20

if age >= 18:
    print("Eligible to vote")
#Executes the block only when the condition evaluates to True.

#2.if-else statement

temperature = 15

if temperature > 25:
    print("It's warm outside")
else:
    print("It's cold outside")
#Provides an alternative execution path when the condition is False.

#3. using if..elif..else chain
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: D")
#Allows testing multiple conditions in sequence.

#4. Nested if Statements

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Access granted")
    else:
        print("Incorrect password")
#An if block can exist inside another for complex logic.

#5. Using Logical Operators in Conditions
age = 25
is_verified = True

if age > 18 and is_verified:
    print("User can proceed")
#Combine multiple conditions using and, or, and not.

#6.Short-Hand if Statement (Single Line)
x = 10

if x > 5: print("x is greater than 5")
#Useful for minimal conditional checks.

#7.Short-Hand if...else (Ternary Expression)
num = 7

result = "Even" if num % 2 == 0 else "Odd"
print(result)  # Output: Odd
#Compact inline conditional assignment.

#8.Checking Multiple Values with in
day = "Sunday"

if day in ["Saturday", "Sunday"]:
    print("Weekend")
else:
    print("Weekday")
#Efficient alternative to chained OR conditions.

#9.Comparing Strings in Conditions
username = "Alice"

if username.lower() == "alice":
    print("Welcome Alice")
#Common technique to handle case-insensitive comparisons.

#10.Using pass in if Statement
value = 5

if value > 0:
    pass  # Placeholder for future logic

print("Program continues...")
#pass acts as a syntactic placeholder to avoid errors for empty blocks.



