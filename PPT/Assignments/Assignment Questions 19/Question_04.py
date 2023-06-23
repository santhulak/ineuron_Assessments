'''Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).

**Example:**
Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
Output : arr[] = {1, 2, 4, 3, 5, 0, 0, 0};

Input : arr[]  = {1, 2, 0, 0, 0, 3, 6};
Output : arr[] = {1, 2, 3, 6, 0, 0, 0};'''

def pushZerosToEnd(arr):
    n = len(arr)
    left = 0
    right = 0

    while right < n:
        if arr[right] != 0:
            arr[left] = arr[right]
            left += 1
        right += 1

    while left < n:
        arr[left] = 0
        left += 1

    return arr
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
result = pushZerosToEnd(arr)
print(result)


arr = [1, 2, 0, 4, 3, 0, 5, 0]
result = pushZerosToEnd(arr)
print(result)


arr = [1, 2, 0, 0, 0, 3, 6]
result = pushZerosToEnd(arr)
print(result)

