text = input("Enter string: ")
width = int(input("Total width: "))
print(text + " " * max(0, width - len(text)))