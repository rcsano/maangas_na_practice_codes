text = input("Enter string: ")
width = int(input("Total width: "))
print("0" * (width - len(text)) + text if width > len(text) else text)