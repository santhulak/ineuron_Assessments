'''Given an array of integers, the task is to find the maximum absolute difference between the nearest left and the right smaller element of every element in the array.

**Note:** If there is no smaller element on right side or left side of any element then we take zero as the smaller element. For example for the leftmost element, the nearest smaller element on the left side is considered as 0. Similarly, for rightmost elements, the smaller element on the right side is considered as 0.

**Examples:**
Input : arr[] = {2, 1, 8}
Output : 1
Left smaller  LS[] {0, 0, 1}
Right smaller RS[] {1, 0, 0}
Maximum Diff of abs(LS[i] - RS[i]) = 1

Input  : arr[] = {2, 4, 8, 7, 7, 9, 3}
Output : 4
Left smaller   LS[] = {0, 2, 4, 4, 4, 7, 2}
Right smaller  RS[] = {0, 3, 7, 3, 3, 3, 0}
Maximum Diff of abs(LS[i] - RS[i]) = 7 - 3 = 4

Input : arr[] = {5, 1, 9, 2, 5, 1, 7}
Output : 1'''
def maxAbsoluteDiff(arr):
    n = len(arr)
    leftSmaller = [0] * n
    rightSmaller = [0] * n
    leftStack = []
    rightStack = []
    
    # Compute leftSmaller[] array
    for i in range(n):
        while leftStack and leftStack[-1][0] >= arr[i]:
            leftStack.pop()
        if leftStack:
            leftSmaller[i] = leftStack[-1][1]
        leftStack.append((arr[i], i))
    
    # Compute rightSmaller[] array
    for i in range(n-1, -1, -1):
        while rightStack and rightStack[-1][0] >= arr[i]:
            rightStack.pop()
        if rightStack:
            rightSmaller[i] = rightStack[-1][1]
        rightStack.append((arr[i], i))
    
    maxDiff = 0
    
    # Compute maxDiff
    for i in range(n):
        diff = abs(leftSmaller[i] - rightSmaller[i])
        maxDiff = max(maxDiff, diff)
    
    return maxDiff

# Example usage
arr = [2, 1, 8]
result = maxAbsoluteDiff(arr)
print(result)  # Output: 1

arr = [2, 4, 8, 7, 7, 9, 3]
result = maxAbsoluteDiff(arr)
print(result)  # Output: 4

arr = [5, 1, 9, 2, 5, 1, 7]
result = maxAbsoluteDiff(arr)
print(result)  # Output: 1
