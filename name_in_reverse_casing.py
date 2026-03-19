full_name = input("Enter your full name: ")
result = ""

for character in full_name:
    if character.islower():
        result += character.upper()
    elif character.isupper():
        result += character.lower()
    else:
        result += character

print(result)