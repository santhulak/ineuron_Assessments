'''
💡 **Sort Colors**

Given an array `nums` with `n` objects colored red, white, or blue, sort them **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

**Example 1:**

```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

```

**Example 2:**

```
Input: nums = [2,0,1]
Output: [0,1,2]

```

**Constraints:**

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.
</aside>'''

def sortColors(nums):
    # Initialize three pointers
    left = 0  # pointer for 0's
    mid = 0  # pointer for 1's
    right = len(nums) - 1  # pointer for 2's

    while mid <= right:
        if nums[mid] == 0:
            # Swap nums[left] and nums[mid]
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            # Swap nums[mid] and nums[right]
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1

    return nums
nums = [2, 0, 2, 1, 1, 0]
print(sortColors(nums))  

nums = [2, 0, 1]
print(sortColors(nums))  
