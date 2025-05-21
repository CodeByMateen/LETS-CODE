def first_non_repeating(text):
    text = text.lower()
    freq = {}
    
    for char in text:
        if char.isalpha():
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
            
    if len(freq) == 0:
        print(1)
        return "No non repeating characters"
    
    for key, value in freq.items():
        if value == 1:
            return key
    
    return "no non-repeating characters"
            
text = "mmaa@tt"
print(first_non_repeating(text))

'''
method 2
'''

def first_non_repeating(text):
    freq = {}

    for char in text:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1

    for char in text:
        if char.isalpha() and freq[char] == 1:
            return char

    return "None"

text = "@mateen"
print(first_non_repeating(text))  # Output: m

'''
method 3
'''

from collections import Counter

def first_non_repeating_counter(text):
    text = text.lower()
    freq = Counter(c for c in text if c.isalpha())  # filter alphabets and count frequency
    
    for char in text:
        if char.isalpha() and freq[char] == 1:
            return char
    
    return "No non-repeating characters"

# Test
print(first_non_repeating_counter("mmaa@ttez"))  # Output: e
print(first_non_repeating_counter("mmaa@tt"))    # Output: No non-repeating characters
