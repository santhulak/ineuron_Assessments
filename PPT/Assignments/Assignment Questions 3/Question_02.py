'''Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:
           ● 0 <= a, b, c, d < n
           ● a, b, c, and d are distinct.
           ● nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]'''

def fourSum(nums, target):
    nums.sort()  # Sort the array in ascending order
    n = len(nums)
    quadruplets = []
    
    for i in range(n - 3):
        # Skip duplicates for the first element of the quadruplet
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, n - 2):
            # Skip duplicates for the second element of the quadruplet
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            left = j + 1
            right = n - 1
            
            while left < right:
                curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                
                if curr_sum == target:
                    quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                    
                    # Skip duplicates for the third and fourth elements of the quadruplet
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
    
    return quadruplets

# Test the function
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = fourSum(nums, target)
print(result)
