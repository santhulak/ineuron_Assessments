'''Given a binary array nums, return *the maximum length of a contiguous subarray with an equal number of* 0 *and* 1.

**Example 1:**

**Input:** nums = [0,1]

**Output:** 2

**Explanation:**

[0, 1] is the longest contiguous subarray with an equal number of 0 and 1.'''

def findMaxLength(nums):
    count = 0
    max_length = 0
    count_dict = {0: -1}  # Initialize count_dict with a count of 0 at index -1

    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1

        if count in count_dict:
            # If the count is already present, calculate the length of the subarray
            max_length = max(max_length, i - count_dict[count])
        else:
            # If the count is encountered for the first time, add it to count_dict
            count_dict[count] = i

    return max_length

nums = [0, 1]
result = findMaxLength(nums)
print(result)
