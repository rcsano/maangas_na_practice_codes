result = float(input("Enter first number: "))

for i in range(2, 11):
    result -= float(input(f"Enter number {i+1}: "))

print(result)