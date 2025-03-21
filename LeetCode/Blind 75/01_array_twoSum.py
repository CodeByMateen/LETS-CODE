# Solution 1 
def twoSum(nums, target):
    num_set = set()

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_set:
            return [nums.index(complement), i]
        num_set.add(num)

print(twoSum([2,7,11,15],9))

# Solution 2
def twoSum(nums, target):
    numsSort = sorted(nums)
    left, right = 0, len(numsSort)-1
    while left<right:
        complement = numsSort[left]+numsSort[right]
        if complement==target:
            return numsSort[left],numsSort[right]
        elif complement<target:
            left+=1
        else:
            right-=1
    return None


print(twoSum([2,7,11,15], 9))
