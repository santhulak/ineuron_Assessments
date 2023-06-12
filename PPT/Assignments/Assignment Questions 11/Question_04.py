'''Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return *this repeated number*.

You must solve the problem **without** modifying the array `nums` and uses only constant extra space.

**Example 1:**

```
Input: nums = [1,3,4,2,2]
Output: 2

```

**Example 2:**
Input: nums = [3,1,3,4,2]
Output: 3

'''

def findDuplicate(nums):
    # Step 1: Find the intersection point of the two pointers
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Step 2: Find the entrance of the cycle
    ptr1 = nums[0]
    ptr2 = slow

    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1

# Example usage

result1 = findDuplicate([1, 3, 4, 2, 2])
print(result1)

result2 = findDuplicate([3,1,3,4,2])
print(result2)