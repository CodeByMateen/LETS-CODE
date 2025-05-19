nums = [1, -3, 0, 5, -2, 0]

positive = negative = zero = 0
for num in nums:
    if num > 0:
        positive +=1
    elif num < 0:
        negative +=1
    else:
        zero +=1
        
print(positive, negative, zero)

# method 2 list comprehension

nums = [1, -3, 0, 5, -2, 0]
print("Positive:", len([n for n in nums if n > 0]))
print("Negative:", len([n for n in nums if n < 0]))
print("Zero:", len([n for n in nums if n == 0]))

# using dictionary

nums = [1, -3, 0, 5, -2, 0]
counts = {"positive": 0, "negative": 0, "zero": 0}

for num in nums:
    if num > 0:
        counts["positive"] += 1
    elif num < 0:
        counts["negative"] += 1
    else:
        counts["zero"] += 1

print(counts)

# another method

from collections import defaultdict

counts = defaultdict(int)

for num in nums:
    if num > 0:
        counts["positive"] += 1
    elif num < 0:
        counts["negative"] += 1
    else:
        counts["zero"] += 1

print(dict(counts))
