user_input = input("Enter a string with leading spaces: ")
index = 0

while index < len(user_input) and user_input[index] == " ":
    index += 1

trimmed_string = user_input[index:]
print(trimmed_string)