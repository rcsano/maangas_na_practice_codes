text = input("Enter string: ")
print("".join(chr(ord(character)+32) if "A"<=character<="Z" else character for character in text))