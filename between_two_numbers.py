num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

for i in range (num_2 - num_1 - 1):
    num_1 += 1
    print(num_1, end=" ")