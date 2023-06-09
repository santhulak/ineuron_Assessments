'''Given an array of integers **arr**, the task is to find maximum element of that array using recursion.

**Example 1:**

Input: arr = {1, 4, 3, -5, -4, 8, 6};
Output: 8

**Example 2:**

Input: arr = {1, 4, 45, 6, 10, -8};
Output: 45'''

def find_maximum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], find_maximum(arr[1:]))
arr1 = [1, 4, 3, -5, -4, 8, 6]
print(find_maximum(arr1))  

arr2 = [1, 4, 45, 6, 10, -8]
print(find_maximum(arr2))  
