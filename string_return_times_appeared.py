text = input("Enter string: ")
sub_text = input("Enter substring: ")
count = 0
sub_length = len(sub_text) # Store the length once

for index in range(len(text) - sub_length + 1):
    if text[index : index + sub_length] == sub_text:
        count += 1
print(count)