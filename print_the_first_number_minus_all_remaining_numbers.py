# Create an empty list to store numbers
numbers = []

# Ask the user to enter 10 numbers
for i in range(10):
    num = float(input("Enter number " + str(i+1) + ": "))
    numbers.append(num)