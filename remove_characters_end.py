text = input("Enter string: ")
suffix = input("Suffix: ")
print(text[:-len(suffix)] if text[-len(suffix):] == suffix else text)