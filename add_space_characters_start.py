text = input("Enter string: ")
width = int(input("Total width: "))
print(" "*(width - len(text)) + text if width > len(text) else text)