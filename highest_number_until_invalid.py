# Empty list
numbers = []

# Loop
while True:
    # Enter number
    try:
        num = float(input("Number: "))
    # Stop if invalid
    except ValueError:
        break
    numbers.append(num)

# Show highest
if numbers:
    print("Highest number:", max(numbers))