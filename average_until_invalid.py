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

# Check the average and display
if numbers:
    print("Average:", sum(numbers)/len(numbers))