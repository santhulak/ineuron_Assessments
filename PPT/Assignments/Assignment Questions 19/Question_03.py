'''
<aside>
💡 3. **Sort an Array**

Given an array of integers `nums`, sort the array in ascending order and return it.

You must solve the problem **without using any built-in** functions in `O(nlog(n))` time complexity and with the smallest space complexity possible.

**Example 1:**

```
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

```

**Example 2:**

```
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

```

**Constraints:**

- `1 <= nums.length <= 5 * 10000`
- `-5 * 104 <= nums[i] <= 5 * 10000`

'''
def sortArray(nums):
    def merge(nums, left, mid, right):
        merged = []
        i, j = left, mid + 1

        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                merged.append(nums[i])
                i += 1
            else:
                merged.append(nums[j])
                j += 1

        while i <= mid:
            merged.append(nums[i])
            i += 1

        while j <= right:
            merged.append(nums[j])
            j += 1

        nums[left:right + 1] = merged

    def mergeSort(nums, left, right):
        if left < right:
            mid = (left + right) // 2
            mergeSort(nums, left, mid)
            mergeSort(nums, mid + 1, right)
            merge(nums, left, mid, right)

    mergeSort(nums, 0, len(nums) - 1)
    return nums
nums = [5, 2, 3, 1]
sorted_nums = sortArray(nums)
print(sorted_nums)


nums = [5, 1, 1, 2, 0, 0]
sorted_nums = sortArray(nums)
print(sorted_nums)


