text = input("Enter string: ")
index = len(text) - 1
while index >= 0 and text[index] == " ":
    index -= 1
print(text[:index+1])