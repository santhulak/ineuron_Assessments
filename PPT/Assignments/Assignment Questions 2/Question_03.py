'''We define a harmonious array as an array where the difference between its maximum value
and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence
among all its possible subsequences.

A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5

Explanation: The longest harmonious subsequence is [3,2,2,2,3].'''
def findLHS(nums):
    freq_map = {}
    max_length = 0

    # Count the frequencies of each number
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    # Check for harmonious subsequence
    for num in freq_map:
        if num + 1 in freq_map:
            length = freq_map[num] + freq_map[num + 1]
            max_length = max(max_length, length)

    return max_length

# Test the function
nums = [1, 3, 2, 2, 5, 2, 3, 7]
result = findLHS(nums)
print(result)
