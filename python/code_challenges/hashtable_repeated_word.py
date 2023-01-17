from data_structures.hashtable import Hashtable


def first_repeated_word(text):
    counts = {}
    words = text.split()

    for word in words:
        word = strip_punc(word)
        if word.lower() in counts:
            return word.lower()
        else:
            counts[word.lower()] = 1


def strip_punc(word):
    new_word = ''
    for char in word:
        if char.isalpha():
            new_word += char
    return new_word
