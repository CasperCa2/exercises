# Write your code here


def word_count(string):
    array = string.split()
    words = len(array)
    if words == 0:
        return 1
    return words
