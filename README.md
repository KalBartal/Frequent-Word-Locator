# Frequent Word Locator

This code provides a solution to the problem of finding the most frequently used words from a given list of words. It takes a list of words as input, and returns a list of the most frequently used words. If the input list is empty, an empty list is returned.

## Function Description

The function `most_frequent_words` takes a list of words as an argument and returns a list of the most frequently used words from the list. 

It does this by maintaining a dictionary (`word_count`) to store each word and its corresponding occurrence. 

The function then iterates through the words list and increases the count for each word if it already exists in the dictionary. 

If the word is not present in the dictionary, it assigns a count of 1. The function then uses two variables (`max_count` and `most_frequent_words`) to store the highest occurrence and the words associated with it. It then iterates through the dictionary and compares each word's count to the `max_count`. 

If the count is greater, the `max_count` is updated to the current word's count and the `most_frequent_words` list is updated to contain only the current word. If the count is equal to the `max_count`, the word is added to the `most_frequent_words` list. 

Finally, the function returns the `most_frequent_words` list. 

## Example

Let's take the following example:

Input: ["test", "testing", "retest", "testing"]

Output: ["testing"]

The `most_frequent_words` function will go through the list of words and store them in the `word_count` dictionary with their corresponding counts. After the loop, the dictionary will look like this:

word_count = {
    "test": 1,
    "testing": 2,
    "retest": 1
}

The function then moves on to the comparison logic. Since `testing` has the highest count (2), the `max_count` is set to 2 and the `most_frequent_words` list is updated to contain only the word `testing`. 

Finally, the function returns the `most_frequent_words` list which contains `["testing"]`.

## Constraints

The words in the list are not necessarily unique or lower-case. The function also assumes that the list of words will only contain strings, and that no string in the list will be shorter than one character.

## Usage

To use the `most_frequent_words` function, simply pass a list of words to the function. The function will return the list of the most frequently used words from the list. If the input list is empty, an empty list will be returned.