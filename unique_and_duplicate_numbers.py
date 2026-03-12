# Empty list
numbers = []
# Loop
while True:
    try:
    # Enter number
        num = float(input("Enter a number: "))
    except:
    # Stop if invalid
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