text = input("Enter string: ")
width = int(input("Total width: "))
print(text + " "*(width-len(text)) if width>len(text) else text)