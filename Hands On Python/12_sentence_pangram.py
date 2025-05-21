# A pangram is a sentence that contains every letter of the alphabet at least once.

import string

def isPangram(sen):
    sen = sen.lower()
    alphabets = set(string.ascii_lowercase)
    letters_in_sen = set(char for char in sen if char.isalpha())
    print(sen)
    print(alphabets)
    print(letters_in_sen)

    if alphabets.issubset(letters_in_sen):
        return "Is Pangram"
    else:
        return "Not Pangram"
    
sentence = "The uick brown fox jumps over the lazy dog"
print(isPangram(sentence))
