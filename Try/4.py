def word_indices(paragraph):
    """
    Takes a paragraph of text and returns a dictionary where each key is a unique word
    and the value is a list of indices where the word appears in the paragraph.
    """
    # Clean and tokenize the paragraph
    words = paragraph.lower().replace('.', '').replace(',', '').split()
    word_dict = {}

    # Iterate through the words and store their indices
    for index, word in enumerate(words):
        if word not in word_dict:
            word_dict[word] = []
        word_dict[word].append(index)

    return word_dict

# Example usage
if __name__ == "__main__":
    paragraph = "This is a test. This test is only a test."
    result = word_indices(paragraph)
    print("Word Indices Dictionary:")
    for word, indices in result.items():
        print(f"{word}: {indices}")