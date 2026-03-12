# Ask the user to enter the first number
num1 = int(input("Enter the first number: "))

# Ask the user to enter the second number
num2 = int(input("Enter the second number: "))

# Check if the second number is not zero
if num2 != 0:

    # Calculate the quotient using floor division
    quotient = num1 // num2

# Display the result
    print("The quotient without decimal is:", quotient)

else:
    print("Division by zero is not allowed.")