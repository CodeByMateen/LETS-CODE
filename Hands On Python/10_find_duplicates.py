# def findDuplicates(nums):
#     seen = set()
#     duplicates = set()
#     for num in nums:
#         if num in seen:
#             duplicates.append(num)
#         else:
#             seen.add(num)
    
#     if len(duplicates) > 0:
#         return duplicates
#     else:
#         return "No duplicates"

# method 2 - withought extra space
'''
def findDuplicates(nums):
    result = []

    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            result.append(index + 1)
        else:
            nums[index] = -nums[index]
            print(nums[index])

    return result

        
# # nums = [4, 3, 2, 7, 8, 2, 3, 1]
# nums = [1, 2, 2]
# print(findDuplicates(nums))
'''

# bonus task - Find duplicates without using extra space AND restore the original array at the end!

def find_duplicates(nums):
    duplicates = []
    
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        
        if nums[index] < 0:
            duplicates.append(index + 1)
        else:
            nums[index] = -nums[index]
            
    # restoring orriginal array
    
    # will not work as it creates copy of list elements
    # for num in nums:
    #     num = abs(num)
    
    # correct way
    for i in range(len(nums)):
        nums[i] = abs(nums[i])
    
    return duplicates
    
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(nums))
print(nums)
