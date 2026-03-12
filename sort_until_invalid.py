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

# Sort lowest to highest
numbers.sort()

# Display sorted
print("Numbers from lowest to highest:", numbers)