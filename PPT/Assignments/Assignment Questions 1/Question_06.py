'''
💡  Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

**Example 1:**
Input: nums = [1,2,3,1]

Output: true

'''

def containsDuplicate(nums):
    num_set = set()

    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)

    return False

# Test the function
nums = [1, 2, 3, 1]
result = containsDuplicate(nums)
print(result)
