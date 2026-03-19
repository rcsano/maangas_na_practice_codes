text = input("Enter string: ")
sub_text = input("Enter substring: ")
found_at = -1

for index in range(len(text) - len(sub_text), -1, -1):
    if text[index : index + len(sub_text)] == sub_text:
        found_at = index
        break

print(found_at if found_at != -1 else "Substring not found")