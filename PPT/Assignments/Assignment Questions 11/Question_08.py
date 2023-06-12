'''Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must appear as many times as it shows in both arrays and you may return the result in **any order**.

**Example 1:**

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

```

**Example 2:**
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.'''

from collections import Counter

def intersect(nums1, nums2):
    # Count the frequency of elements in nums1
    nums1_count = Counter(nums1)
    
    # Initialize the result list
    result = []
    
    # Iterate over elements in nums2
    for num in nums2:
        # If the element is present in nums1 and its count is positive
        if num in nums1_count and nums1_count[num] > 0:
            # Add the element to the result list
            result.append(num)
            
            # Decrement the count of the element in nums1
            nums1_count[num] -= 1
    
    return result


# Example usage
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = intersect(nums1, nums2)
print(result)
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
result = intersect(nums1, nums2)
print(result)