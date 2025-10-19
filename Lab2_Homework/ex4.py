def convert_to_snake_case(text):
    if not text:
        return ""
    
    result = [text[0].lower()]
    for char in text[1:]:
        if char.isupper():
            result.append('_')
        result.append(char.lower())
        
    return "".join(result)

camel_case_string = input("Enter a string in UpperCamelCase: ")
snake_case_string = convert_to_snake_case(camel_case_string)
print(f"The converted string is: {snake_case_string}")