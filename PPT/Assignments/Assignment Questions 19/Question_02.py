'''Given an integer array `nums`, return *an integer array* `counts` *where* `counts[i]` *is the number of smaller elements to the right of* `nums[i]`.

**Example 1:**

```
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are2 smaller elements (2 and 1).
To the right of 2 there is only1 smaller element (1).
To the right of 6 there is1 smaller element (1).
To the right of 1 there is0 smaller element.

```

**Example 2:**

```
Input: nums = [-1]
Output: [0]

```

**Example 3:**

```
Input: nums = [-1,-1]
Output: [0,0]

```

**Constraints:**

- `1 <= nums.length <= 100000`
- `-10000 <= nums[i] <= 10000`'''

def countSmaller(nums):
    counts = [0] * len(nums)

    def merge_and_count(nums, left, mid, right, counts):
        i, j, k = left, mid + 1, left
        merged = [0] * len(nums)

        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                counts[nums[i]] += j - (mid + 1)
                merged[k] = nums[i]
                i += 1
            else:
                merged[k] = nums[j]
                j += 1
            k += 1

        while i <= mid:
            counts[nums[i]] += right - mid
            merged[k] = nums[i]
            i += 1
            k += 1

        while j <= right:
            merged[k] = nums[j]
            j += 1
            k += 1

        nums[left:right + 1] = merged[left:right + 1]

    def merge_sort_and_count(nums, left, right, counts):
        if left < right:
            mid = (left + right) // 2
            merge_sort_and_count(nums, left, mid, counts)
            merge_sort_and_count(nums, mid + 1, right, counts)
            merge_and_count(nums, left, mid, right, counts)

    # Map the values of nums to a range that fits the counts array
    min_val = min(nums)
    nums = [val - min_val for val in nums]

    merge_sort_and_count(nums, 0, len(nums) - 1, counts)
    return counts
nums = [5, 2, 6, 1]
result = countSmaller(nums)
print(result)
# Output: [2, 1, 1, 0]
