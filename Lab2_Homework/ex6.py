import re

def extract_first_number(text):
    match = re.search(r'\d+', text)
    if match:
        return int(match.group(0))
    else:
        return None

text1 = "An apple is 123 USD"
text2 = "abc456xyz"
text3 = "No numbers here"

print(f"Text: '{text1}' -> Extracted number: {extract_first_number(text1)}")
print(f"Text: '{text2}' -> Extracted number: {extract_first_number(text2)}")
print(f"Text: '{text3}' -> Extracted number: {extract_first_number(text3)}")