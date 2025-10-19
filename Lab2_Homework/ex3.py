substring = input("Enter the substring to search for: ")
main_string = input("Enter the main string to search in: ")

occurrences = main_string.count(substring)

print(f"The substring '{substring}' appears {occurrences} time(s) in the main string.")