'''
💡  Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

Note that you must do this in-place without making a copy of the array.

**Example 1:**
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

'''
def moveZeroes(nums):
    i = 0

    # Iterate through the array and move non-zero elements to the front
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i] = nums[j]
            i += 1

    # Fill the remaining elements with zeros
    while i < len(nums):
        nums[i] = 0
        i += 1

# Test the function
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)
