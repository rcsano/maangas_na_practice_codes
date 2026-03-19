text = input("Enter string: ")
sub_text = input("Enter substring: ")
found_index = -1

for index in range(0, len(text) - len(sub_text) + 1):
    if text[index : index + len(sub_text)] == sub_text:
        found_index = index
        break

print(found_index if found_index != -1 else "Substring not found")