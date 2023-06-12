'''Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

```

**Example 2:**

```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

```

**Example 3:**
Input: nums = [], target = 0
Output: [-1,-1]'''

def searchRange(nums, target):
    left = findLeftmostIndex(nums, target)
    right = findRightmostIndex(nums, target)

    return [left, right]


def findLeftmostIndex(nums, target):
    left = 0
    right = len(nums) - 1
    index = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] >= target:
            right = mid - 1
            if nums[mid] == target:
                index = mid
        else:
            left = mid + 1

    return index


def findRightmostIndex(nums, target):
    left = 0
    right = len(nums) - 1
    index = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] <= target:
            left = mid + 1
            if nums[mid] == target:
                index = mid
        else:
            right = mid - 1

    return index


# Example usage
nums = [5, 7, 7, 8, 8, 10]
target = 8
result = searchRange(nums, target)
print(result)

nums = [5,7,7,8,8,10]
target = 6
result = searchRange(nums, target)
print(result)
nums = []
target = 0
result = searchRange(nums, target)
print(result)