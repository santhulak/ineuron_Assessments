'''
💡 **Rearrange array in alternating positive & negative items with O(1) extra space**

Given an **array of positive** and **negative numbers**, arrange them in an **alternate** fashion such that every positive number is followed by a negative and vice-versa maintaining the **order of appearance**. The number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear at the end of the array.

**Examples:**

> Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}
> 
'''
def rearrangeArray(arr):
    n = len(arr)

    # Partition the array into positive and negative numbers
    partitionIndex = 0
    for i in range(n):
        if arr[i] < 0:
            arr[i], arr[partitionIndex] = arr[partitionIndex], arr[i]
            partitionIndex += 1

    # Rearrange the array by alternating positive and negative numbers
    positiveIndex = partitionIndex
    negativeIndex = 0

    while positiveIndex < n and negativeIndex < positiveIndex and arr[negativeIndex] < 0:
        arr[positiveIndex], arr[negativeIndex] = arr[negativeIndex], arr[positiveIndex]
        positiveIndex += 1
        negativeIndex += 2

    return arr
arr = [1, 2, 3, -4, -1, 4]
result = rearrangeArray(arr)
print(result)


arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
result = rearrangeArray(arr)
print(result)



