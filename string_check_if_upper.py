text = input("Enter string: ")
print(any("A" <= c <= "Z" for c in text) and not any("a" <= c <= "z" for c in text))