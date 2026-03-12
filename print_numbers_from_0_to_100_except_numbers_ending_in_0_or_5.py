# Loop from 0 to 100
for number in range(0, 101):

    # Get the last digit of the number
    last_digit = number % 10

    # Check if the number does NOT end with 0 or 5
    if last_digit != 0 and last_digit != 5:

        # Print the number
        print(number)