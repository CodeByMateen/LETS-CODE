# Solution 1 self
nums = [1,1,1,3,3,4,3,2,4,2]
numnew=[]
for i in nums:
    if i in numnew:
        print("duplicate found of", i)
    else:
        numnew.append(i)
        
# Solution 2 
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
num_set = set()
for i in nums:
    if i in num_set:
        print("Duplicate found of", i)
    else:
        num_set.add(i)
