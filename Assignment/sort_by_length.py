# Create a function that ta kes a list of words as input and returns a new list
# with the words sorted by their length


def sort_by_length(words):
    return sorted(words, key=len)

words = ["sandra", "faith", "mercy", "a", "joan"]
sorted_words = sort_by_length(words)
print(sorted_words)