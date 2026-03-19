full_name = input("Enter your full name: ")
words = full_name.split()
result = " "

for word in words:
    word = word.lower()
    result += chr(ord(word[0]) - 32) + word[1:]

print(result)
