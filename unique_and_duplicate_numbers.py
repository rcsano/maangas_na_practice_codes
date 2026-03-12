# Empty list
numbers = []

# Loop
while True:
    try:
    # Enter number
        num = float(input("Enter a number: "))
    # Stop if invalid
    except ValueError:
        break

# Check if number exists on list
    if num in numbers:
        # Appeared
        print("Duplicate")
    else:
    # New
        print("Unique")
    # Store
        numbers.append(num)