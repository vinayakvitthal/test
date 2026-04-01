#1. Basic while Loop
count = 1

while count <= 5:
    print(count)
    count += 1
#Executes repeatedly as long as the condition evaluates to True.

#2. Decrementing Counter in while Loop
number = 5

while number > 0:
    print(number)
    number -= 1
#Commonly used for countdown logic.

#3. Using while with User Input
user_input = ""

while user_input != "exit":
    user_input = input("Type 'exit' to stop: ")
#Loop continues until a specific input condition is met.

#4. Infinite while Loop
while True:
    print("Running...")
#Creates an endless loop unless interrupted with break.

#5. Breaking a while Loop
count = 0

while True:
    if count == 3:
        break
    print(count)
    count += 1
#break terminates the loop immediately.

#6. Using continue in while Loop
number = 0

while number < 5:
    number += 1
    if number == 3:
        continue
    print(number)
#Skips the current iteration and proceeds to the next cycle.

#7. while Loop with else Clause
x = 0

while x < 3:
    print(x)
    x += 1
else:
    print("Loop completed normally")
#The else block runs if the loop ends without encountering break.

#8. Simulating do-while Loop Behavior
count = 0

while True:
    print("Executing at least once")
    count += 1
    if count == 3:
        break
#Python does not have a native do-while, but this pattern replicates it.

#9. Nested while Loops
i = 1

while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
#A while loop inside another while loop.

#10. Using while for Input Validation
age = -1

while age < 0:
    age = int(input("Enter a positive age: "))

print("Valid age entered:", age)
#Ensures user input meets required constraints before proceeding.


