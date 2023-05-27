'''
**Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
**Example:**
Input: nums = [2,7,11,15], target = 9
Output0 [0,1]

**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1][

'''
def twoSum(nums, target):
    num_dict = {}  # Create an empty dictionary to store numbers and their indices

    # Iterate through the list
    for i, num in enumerate(nums):
        complement = target - num  # Calculate the complement of the current number

        # Check if the complement exists in the dictionary
        if complement in num_dict:
            return [num_dict[complement], i]  # Return the indices if complement is found

        num_dict[num] = i  # Add the number and its index to the dictionary

    # If no solution is found, return an empty list
    return []

# Test the function
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)

