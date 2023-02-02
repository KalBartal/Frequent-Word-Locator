# Frequent Word Locator
# Problem:
# Given a list of words, write a function that returns the most frequently used words, using a dictionary.
#
# Example:
# Input: ["test", "testing", "retest", "testing"]
#
# Output: ["testing"]
#
# Constraints:
# – The words are not necessarily unique or lower-case.
# – The list of words may be empty, in which case the function should return an empty list.
# – Assume that the words in the list are all strings and longer than one character.


# Function to find the most frequent words in a list
def most_frequent_words(words):
    # Dictionary to store words and corresponding occurrence
    word_count = {}

    # Iterate through words list
    for word in words:
        # Check if word is already present in the dictionary
        if word in word_count:
            # If yes, increment count by 1
            word_count[word] += 1
        # If no, set count to 1
        else:
            word_count[word] = 1

    # Variables to store highest occurrence and corresponding words
    max_count = 0
    most_frequent_words = []

    # Iterate through dictionary
    for word in word_count:
        # Compare current word's count to maximum count
        if word_count[word] > max_count:
            # If count is greater, set max_count to current word's count
            max_count = word_count[word]
            most_frequent_words = [word]
        elif word_count[word] == max_count:
            # If count is equal, add word to the most_frequent_words list
            most_frequent_words.append(word)

    # Return most frequent words
    return most_frequent_words
