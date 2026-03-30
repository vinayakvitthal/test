#Using print() for Standard Output

print("Hello, Python!")
print(100)
print(3.14)

#Printing Multiple Values

name = "Alice"
age = 30

print(name, age)  
# Output: Alice 30

#Customizing Output with sep and end

print("Python", "is", "powerful", sep=" - ", end="!")
# Output: Python - is - powerful!

# Formatted Output using f-strings
name = "Bob"
score = 88

print(f"Student {name} scored {score} marks.")
# Output: Student Bob scored 88 marks.

#Using str.format() Method
product = "Laptop"
price = 1200

print("The price of {} is ${}".format(product, price))
# Output: The price of Laptop is $1200

#String Formatting with Old-Style % Operator

item = "Book"
quantity = 5

print("You bought %d %s(s)." % (quantity, item))
# Output: You bought 5 Book(s).

#Using input() to Receive User Input
name = input("Enter your name: ")
print("Hello,", name)

#Converting Input to Required Data Type
age = int(input("Enter your age: "))

print(f"You will be {age + 1} next year.")

#Reading Multiple Inputs in One Line

numbers = input("Enter two numbers: ").split()

num1 = int(numbers[0])
num2 = int(numbers[1])

print(num1 + num2)

#Redirecting Output to a File

with open("output.txt", "w") as file:
    print("This text goes into the file.", file=file)

print("Data successfully written to output.txt")