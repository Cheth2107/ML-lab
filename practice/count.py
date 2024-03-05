// Python Program to count words in a string using dictionary

def count_words(input_string):
    word_count = {}
    # Split the string into words
    words = input_string.split()

    # Count the occurrences of each word
    for word in words:
        # Remove punctuation if any
        word = word.strip(",.!?;:\"").lower()
        # Increment the count of the word
        if word:
            word_count[word] = word_count.get(word, 0) + 1

    return word_count

# Example usage:
input_string = "This is a sample string. This string is used to demonstrate word count in Python."
word_count = count_words(input_string)
print("Word count in the string:")
for word, count in word_count.items():
    print(f"'{word}': {count}")
