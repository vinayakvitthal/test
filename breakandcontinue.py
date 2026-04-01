#1. Using break to Exit a Loop Early
for number in range(1, 10):
    if number == 5:
        break
    print(number)
#The loop stops immediately when the break statement is encountered.

#2. Using continue to Skip an Iteration
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
#The current iteration is skipped, and the loop proceeds with the next cycle.

#3. break in a while Loop
count = 0

while True:
    if count == 3:
        break
    print(count)
    count += 1
#Demonstrates breaking out of an infinite loop.

#4. continue in a while Loop
num = 0

while num < 5:
    num += 1
    if num == 2:
        continue
    print(num)
#Illustrates bypassing specific values.

#5. Using break in Nested Loops
for i in range(3):
    for j in range(5):
        if j == 2:
            break
        print(f"i={i}, j={j}")
#break exits only the inner loop.

#6. Using Flag with break for Controlled Exit
found = False

for number in range(10):
    if number == 7:
        found = True
        break

print("Found:", found)
#Flag variables help manage complex exit logic.

#7. break + else Interaction
for n in range(5):
    if n == 10:
        break
else:
    print("Loop completed without break")
#The else executes only if the loop does not terminate via break.

#8. continue for Input Filtering
for char in "python123":
    if char.isdigit():
        continue
    print(char)
#Useful for skipping unwanted values during iteration.

#9. Breaking Based on User Input
while True:
    user_input = input("Enter 'q' to quit: ")
    if user_input.lower() == 'q':
        break
#Common pattern for controlled loop termination.

#10. Performance Use Case with continue
numbers = [1, -2, 3, -4, 5]

for num in numbers:
    if num < 0:
        continue
    print(num)
#Prevents unnecessary processing for invalid data, improving loop efficiency.