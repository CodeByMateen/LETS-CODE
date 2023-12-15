# Solution 1
product=1
l = [1,2,3,4]
for num in l:
  product*=num

print(product)

B=[product//i for i in l]
print(B)

# Solution 2
def productExceptSelf(nums):
  n = len(nums)
  result = [1] * n

  # Calculate left products and store them in the result array
  left_product = 1
  for i in range(n):
      result[i] *= left_product
      left_product *= nums[i]

  # Calculate right products and multiply with the result array
  right_product = 1
  for i in range(n - 1, -1, -1):
      result[i] *= right_product
      right_product *= nums[i]

  return result

# Example usage:
nums1 = [1, 2, 3, 4]
print(productExceptSelf(nums1))  # Output: [24, 12, 8, 6]

nums2 = [-1, 1, 0, -3, 3]
print(productExceptSelf(nums2))  # Output: [0, 0, 9, 0, 0]
