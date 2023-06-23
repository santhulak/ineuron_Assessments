'''Given an integer array `nums`, return *the maximum difference between two successive elements in its sorted form*. If the array contains less than two elements, return `0`.

You must write an algorithm that runs in linear time and uses linear extra space.

**Example 1:**

```
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

```

**Example 2:**

```
Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.

```

**Constraints:**

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`'''

def maximumGap(nums):
    if len(nums) < 2:
        return 0

    # Find the maximum element in nums
    max_num = max(nums)

    # Perform Radix Sort
    exp = 1
    output = [0] * len(nums)

    while max_num // exp > 0:
        count = [0] * 10

        for num in nums:
            digit = (num // exp) % 10
            count[digit] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            digit = (num // exp) % 10
            output[count[digit] - 1] = num
            count[digit] -= 1

        nums = output.copy()
        exp *= 10

    # Find the maximum difference
    max_diff = 0
    for i in range(1, len(nums)):
        max_diff = max(max_diff, nums[i] - nums[i - 1])

    return max_diff


nums = [3, 6, 9, 1]
print(maximumGap(nums))  
nums = [10]
print(maximumGap(nums)) 