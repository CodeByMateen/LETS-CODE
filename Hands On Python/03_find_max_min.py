nums = [4, 10, -1, 0, 7]

max_val = min_val = nums[0]

for num in nums:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Max =", max_val)
print("Min =", min_val)
