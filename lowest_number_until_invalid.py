# Empty list
numbers = []

# Loop until invalid
while True:
    # Enter number
    try:
        num = float(input("Enter a number: "))
    # Stop if invalid
    except ValueError:
        break
    numbers.append(num)

# Show lowest
if numbers:
    print("Lowest number:", min(numbers))
