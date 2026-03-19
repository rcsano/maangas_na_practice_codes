text = input("Enter string: ")
print("".join(chr(ord(c)+32) if "A"<=c<="Z" else c for c in text))