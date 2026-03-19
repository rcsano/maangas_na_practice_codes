text = input("Enter string: ")
print(any("a" <= character <= "z" for character in text) and not any("A" <= character <= "Z" for character in text))