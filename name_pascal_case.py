full_name = input("Enter full name: ")
print("".join(word.capitalize() for word in full_name.split()))