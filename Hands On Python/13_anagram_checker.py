'''
After clearing conditions below, we can say two strings are anagram:

- Remove spaces and punctuation.

- Lowercase both strings.

- Compare frequency of characters.
'''

def isAnagram(str1, str2):
    def cleanString(s):
        return "".join(char.lower() for char in s if char.isalpha())
    
    str1 = cleanString(str1)
    str2 = cleanString(str2)
    
    if len(str1) != len(str2):
        return False
    
    return sorted(str1) == sorted(str2)
    
str1 = "Doom"
str2 = "Mood"

print(isAnagram(str1, str2))

'''
method 2
'''

from collections import Counter
import string

def isAnagram(str1, str2):
    clean = lambda s: "".join(c.lower() for c in s if c.isalpha())
    return Counter(clean(str1)) == Counter(clean(str2))

print(isAnagram("Dormitory", "Dirty room"))  # ✅ True
