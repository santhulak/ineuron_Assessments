'''
Given a **circular integer array** `nums` of length `n`, return *the maximum possible sum of a non-empty **subarray** of* `nums`.

A **circular array** means the end of the array connects to the beginning of the array. Formally, the next element of `nums[i]` is `nums[(i + 1) % n]` and the previous element of `nums[i]` is `nums[(i - 1 + n) % n]`.

A **subarray** may only include each element of the fixed buffer `nums` at most once. Formally, for a subarray `nums[i], nums[i + 1], ..., nums[j]`, there does not exist `i <= k1`, `k2 <= j` with `k1 % n == k2 % n`.

**Example 1:**

```
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

```

**Example 2:**
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
'''

def maxSubarraySumCircular(nums):
    total_sum = 0
    max_sum = float('-inf')
    current_max = 0
    min_sum = float('inf')
    current_min = 0
    
    for num in nums:
        total_sum += num
        # Calculate maximum sum subarray (case 1)
        current_max = max(current_max + num, num)
        max_sum = max(max_sum, current_max)
        # Calculate minimum sum subarray (case 2)
        current_min = min(current_min + num, num)
        min_sum = min(min_sum, current_min)
    
    # Handle the case when all elements are negative
    if max_sum < 0:
        return max_sum
    
    # Return the maximum of the two cases
    return max(max_sum, total_sum - min_sum)

# Example usage
nums = [1, -2, 3, -2]
result = maxSubarraySumCircular(nums)
print(result)  # Output: 3

nums = [5, -3, 5]
result = maxSubarraySumCircular(nums)
print(result)  # Output: 10

nums = [-3, -2, -3]
result = maxSubarraySumCircular(nums)
print(result)  # Output: -2
