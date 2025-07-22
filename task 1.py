# Simple Calculator - Built during my CodSoft Internship

print("Welcome to the Simple Calculator!\n")

# -------------------------------------------------------
# Name     : [Abhinav Pal]
# Project  : Simple Calculator in Python
# Role     : Intern @ CodSoft
# Description:
#     This is a basic calculator that performs 
#     addition, subtraction, multiplication, and division
#     based on user input. Built as a part of my internship
#     learning journey at CodSoft.
# -------------------------------------------------------


# Take user input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print(" Please enter valid numbers only.")
    exit()

print("\nChoose an operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter your choice (1/2/3/4): ")

#calculation based on choice
if choice == '1':
    result = num1 + num2
    op = '+'
elif choice == '2':
    result = num1 - num2
    op = '-'
elif choice == '3':
    result = num1 * num2
    op = '*'
elif choice == '4':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    result = num1 / num2
    op = '/'
else:
    print("Invalid choice. Please select 1, 2, 3, or 4.")
    exit()

print(f"\n Result: {num1} {op} {num2} = {result}")
