# Empty list
numbers = []

# Input 10 numbers
for i in range(10):
    num = float(input(f"Number {i+1}: "))
    numbers.append(num)

# Store duplicate
shown = []

# Print the duplicates
for num in numbers:
    if numbers.count(num) > 1 and num not in shown:
        print(num)
        shown.append(num)