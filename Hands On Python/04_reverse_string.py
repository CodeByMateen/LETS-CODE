text = "Mateen"

reversed_text = ""

for i in range(len(text)-1, -1, -1):
    reversed_text += text[i]
    
print(reversed_text)

# method 2

text = "Mateen"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text # Prepend

print(reversed_text)
