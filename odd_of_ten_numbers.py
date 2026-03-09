counter = 0
for i in range (10) :
# Input
    num = float(input(f"Enter number {i+1}: "))
# Check if odd
    if num % 2 != 0 :
        counter += 1
# Print
print(counter)