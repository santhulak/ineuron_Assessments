'''<aside>
💡 A permutation of an array of integers is an arrangement of its members into a
sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr:
[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater
permutation of its integer. More formally, if all the permutations of the array are
sorted in one container according to their lexicographical order, then the next
permutation of that array is the permutation that follows it in the sorted container.

If such an arrangement is not possible, the array must be rearranged as the
lowest possible order (i.e., sorted in ascending order).

● For example, the next permutation of arr = [1,2,3] is [1,3,2].
● Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
● While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not
have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.

**Example 1:**
Input: nums = [1,2,3]
Output: [1,3,2]

</aside>'''
def nextPermutation(nums):
    n = len(nums)
    i = n - 2
    
    # Find the first pair of adjacent elements where nums[i] < nums[i+1]
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    
    if i >= 0:
        j = n - 1
        
        # Find the smallest element to the right of nums[i] that is larger than nums[i]
        while j > i and nums[j] <= nums[i]:
            j -= 1
        
        # Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]
    
    # Reverse the elements to the right of nums[i]
    left = i + 1
    right = n - 1
    
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Test the function
nums = [1, 2, 3]
nextPermutation(nums)
print(nums)
