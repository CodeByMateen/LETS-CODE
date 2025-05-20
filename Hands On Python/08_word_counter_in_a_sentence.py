# text = "Mateen is rising to rule and Mateen never quits"
text = input("Enter the text with frequent words separated by spaces\n: ")
word_count = {}
word_list = text.split(" ")

for word in word_list:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        
print(word_count)

for word, count in word_count.items():
    print(f"{word}: {count}")
