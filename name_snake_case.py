full_name = input("Enter full name: ")
words = full_name.split()
result = " "

for index in range(len(words)):
    word = words[index].lower()
    result += word
    if index != len(words) - 1:
        result += "_"

print(result)