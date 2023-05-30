'''Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

*Return the array in the form* [x1,y1,x2,y2,...,xn,yn].

**Example 1:**

**Input:** nums = [2,5,1,3,4,7], n = 3

**Output:** [2,3,5,4,1,7]

**Explanation:** Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].'''
def shuffle(nums, n):
    result = []
    i = 0  # Pointer for the first half of the array
    j = n  # Pointer for the second half of the array

    while i < n and j < 2 * n:
        result.append(nums[i])  # Add the element from the first half
        result.append(nums[j])  # Add the element from the second half
        i += 1
        j += 1

    return result

# Test the function
nums = [2, 5, 1, 3, 4, 7]
n = 3
result = shuffle(nums, n)
print(result)
