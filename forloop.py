#1.1. Basic for Loop with a Sequence
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
#Iterates over each element in a sequence.

#2. Using range() in for Loop
for i in range(5):
    print(i)
#Generates numbers from 0 to 4 by default.

#3. Custom Start and Step with range()
for i in range(2, 10, 2):
    print(i)
#Format: range(start, stop, step)
#Output: 2, 4, 6, 8

#4. Iterating Through a String
word = "Python"

for char in word:
    print(char)
#Processes each character individually.

#5. Using for with Index via enumerate()
languages = ["Python", "Java", "C++"]

for index, lang in enumerate(languages):
    print(index, lang)
#Provides both index and value during iteration.

#6. Nested for Loops
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
#A loop inside another loop, commonly used for matrices and grids.

#7. Using break in for Loop
for number in range(1, 10):
    if number == 5:
        break
    print(number)
#Terminates the loop when the condition is met.

#8. Using continue in for Loop
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
#Skips the current iteration without stopping the loop.

#9. for Loop with else Clause
for num in range(3):
    print(num)
else:
    print("Loop completed successfully")
#The else block executes when the loop finishes normally (not broken).

#10. Iterating Over Dictionaries
student = {"name": "Alice", "age": 22, "grade": "A"}

for key, value in student.items():
    print(key, ":", value)
#Allows iteration over keys, values, or key–value pairs.



