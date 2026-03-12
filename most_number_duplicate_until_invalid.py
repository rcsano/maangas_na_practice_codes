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

# Check duplicate
most = max(numbers, key=numbers.count)
# Print most duplicated number
print("Number that has the most duplicates:", most)
