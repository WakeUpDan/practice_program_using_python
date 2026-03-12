# Ask the user for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Determine the smaller and larger number
if num1 < num2:
    start = num1
    end = num2
else:
    start = num2
    end = num1