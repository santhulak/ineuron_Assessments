'''
💡  **Merge two sorted arrays**

Given two sorted arrays, the task is to merge them in a sorted manner.

**Examples:**

> Input: arr1[] = { 1, 3, 4, 5}, arr2[] = {2, 4, 6, 8} 
Output: arr3[] = {1, 2, 3, 4, 4, 5, 6, 8}

Input: arr1[] = { 5, 8, 9}, arr2[] = {4, 7, 8}
Output: arr3[] = {4, 5, 7, 8, 8, 9}
> 
'''
def mergeArrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    merged = []
    i = 0
    j = 0

    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < n1:
        merged.append(arr1[i])
        i += 1

    while j < n2:
        merged.append(arr2[j])
        j += 1

    return merged

arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]
result = mergeArrays(arr1, arr2)
print(result)


arr1 = [5, 8, 9]
arr2 = [4, 7, 8]
result = mergeArrays(arr1, arr2)
print(result)


