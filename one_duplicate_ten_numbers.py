numbers = []
num_shown = []

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

for num in numbers:
    if num not in num_shown:
        print(num)
        num_shown.append(num)