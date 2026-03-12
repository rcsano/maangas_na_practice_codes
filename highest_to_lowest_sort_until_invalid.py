# Empty list
numbers = []

# Loop
while True:
    # Enter number
    try:
        num = float(input("Enter a number: "))
    # Stop if invalid
    except ValueError:
        break
    numbers.append(num)

# Sort highest to lowest
numbers.sort(reverse=True)

# Display sorted
print("Numbers from highest to lowest:", numbers)