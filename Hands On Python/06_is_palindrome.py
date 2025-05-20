text = "Madam"
text = text.lower()

# reversed_text = text[::-1]

# another way
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text
    
print(reversed_text)
isPalindrome = True if text == reversed_text else False

print(isPalindrome)

'''
# more shorter

text = "Madam"
isPalindrome = text.lower() == text.lower()[::-1]
print(isPalindrome)

'''

# for numbers
nums = 89798

numsPalindrome = str(nums) == str(nums)[::-1]

print(numsPalindrome)
