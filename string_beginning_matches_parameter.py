text = input("Enter string: ")
prefix = input("Prefix to check: ")
print(text[:len(prefix)] == prefix)