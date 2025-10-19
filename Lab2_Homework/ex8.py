def count_words(text):
    if not text:
        return 0
    words = text.split(' ')
    return len(words)

example_text = "I have a Python exam"
word_count = count_words(example_text)

print(f"The text: '{example_text}'")
print(f"Number of words: {word_count}")