'''Given an array of integers arr, return *true if and only if it is a valid mountain array*.

Recall that arr is a mountain array if and only if:

- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
    - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
    **Example 1:**

**Input:** arr = [2,1]

**Output:**

false
    '''

def validMountainArray(arr):
    n = len(arr)
    if n < 3:
        return False

    i = 0

    # Check for increasing order
    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1

    # Peak should not be the first or last element
    if i == 0 or i == n - 1:
        return False

    # Check for decreasing order
    while i < n - 1 and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1

arr = [2, 1]
result = validMountainArray(arr)
print(result)
