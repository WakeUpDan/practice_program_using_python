# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check if divisor is zero
if num2 != 0:

    # Calculate the remainder
    remainder = num1 % num2

# Display the remainder
    print("The remainder when", num1, "is divided by", num2, "is:", remainder)

else:
    print("Cannot divide by zero.")