text = input("Enter string: ")
suffix = input("Suffix to check: ")
print(text[-len(suffix):] == suffix)