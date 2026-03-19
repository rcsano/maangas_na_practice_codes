text = input("Enter string: ")
print("".join(chr(ord(character) - 32) if "a" <= character <= "z" else character for character in text))