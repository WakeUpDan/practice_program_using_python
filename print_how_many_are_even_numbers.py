# Initialize counter for even numbers
even_count = 0

# Loop 10 times to get numbers from user
for i in range(10):

    number = int(input("Enter number " + str(i+1) + ": "))

    # Check if the number is even
    if number % 2 == 0:
        even_count = even_count + 1

# Print total even numbers
print("Total even numbers entered:", even_count)