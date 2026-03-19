text = input("Enter string: ")
width = int(input("Total width: "))
center = width - len(text)
print(" " * (center // 2) + text + " " * (center - center // 2))