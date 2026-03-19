text = input("Enter string: ")
print(any("A" <= character <= "Z" for character in text) and not any("a" <= character <= "z" for character in text))