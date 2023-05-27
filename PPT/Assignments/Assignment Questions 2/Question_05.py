'''Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6'''
def maximumProduct(nums):
    nums.sort()
    n = len(nums)
    return max(nums[0] * nums[1] * nums[n-1], nums[n-3] * nums[n-2] * nums[n-1])

# Test the function
nums = [1, 2, 3]
result = maximumProduct(nums)
print(result)
