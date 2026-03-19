text = input("Enter string: ")
prefix = input("Prefix to remove: ")
print(text[len(prefix):] if text[:len(prefix)] == prefix else text)