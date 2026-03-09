odd_count = 0

for i in range (10) :
    num = float(input(f"Enter number {i+1}: "))
    if num % 2 != 0 :
        odd_count += 1

print(odd_count)