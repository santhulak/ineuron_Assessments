'''Given an integer array nums of length n and an integer target, find three integers
in nums such that the sum is closest to the target.
Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2

Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).'''

def threeSumClosest(nums, target):
    nums.sort()  # Sort the array in ascending order
    n = len(nums)
    closest_sum = float('inf')  # Initialize the closest sum to positive infinity
    
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            
            if curr_sum == target:
                return curr_sum
            
            if abs(curr_sum - target) < abs(closest_sum - target):
                closest_sum = curr_sum
            
            if curr_sum < target:
                left += 1
            else:
                right -= 1
    
    return closest_sum

# Test the function
nums = [-1, 2, 1, -4]
target = 1
result = threeSumClosest(nums, target)
print(result)
