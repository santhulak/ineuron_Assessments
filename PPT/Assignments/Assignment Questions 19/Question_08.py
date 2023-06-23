'''
💡 **Intersection of Two Arrays II**

Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must appear as many times as it shows in both arrays and you may return the result in **any order**.

**Example 1:**

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

```

**Example 2:**

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

```

**Constraints:**

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`
'''
def intersect(nums1, nums2):
    hashmap = {}
    intersection = []

    # Store the frequency of each element in nums1
    for num in nums1:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1

    # Find common elements in nums2 and decrement their frequencies
    for num in nums2:
        if num in hashmap and hashmap[num] > 0:
            intersection.append(num)
            hashmap[num] -= 1

    return intersection
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = intersect(nums1, nums2)
print(result)


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
result = intersect(nums1, nums2)
print(result)

