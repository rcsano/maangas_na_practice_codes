# Ask for the first number
result = float(input("Enter first number: "))
# Ask for the remaining numbers and subtract it to the first
for i in range(2, 11):
    result -= float(input(f"Enter number {i+1}: "))
# Print
print(result)