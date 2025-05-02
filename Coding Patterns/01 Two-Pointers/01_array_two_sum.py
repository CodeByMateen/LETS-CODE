l = [2, 3, 5, 7, 8, 9]
target = 10

# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         print(l[i]+l[j])

# nums = [2, 7, 11, 15]
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         print(f"Checking: {nums[i]} + {nums[j]} = {nums[i] + nums[j]}")

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] + l[j] == target:
            print([i, j])
            
