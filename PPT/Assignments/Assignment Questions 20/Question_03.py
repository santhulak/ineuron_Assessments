'''<aside>
💡 Question-3

Given an array of size n. The problem is to check whether the given array can represent the level order traversal of a Binary Search Tree or not.

Examples:

Input1 : arr[] = {7, 4, 12, 3, 6, 8, 1, 5, 10}

Output1 : Yes

For the given arr[], the Binary Search Tree is:

            7

         /    \

       4     12

     /  \     /

    3   6  8

   /    /     \

 1    5      10

Input2 : arr[] = {11, 6, 13, 5, 12, 10}

Output2 : No

The given arr[] does not represent the level order traversal of a BST.

</aside>'''
def isLevelOrderBST(arr):
    if len(arr) <= 2:
        return "Yes"

    stack = []
    root = float('-inf')
    n = len(arr)

    for i in range(1, n):
        if arr[i] < stack[-1]:
            return "No"

        while stack and arr[i] > stack[-1]:
            root = stack.pop()

        stack.append(arr[i])

    while stack:
        if stack.pop() < root:
            return "No"

    return "Yes"

# Example usage
arr1 = [7, 4, 12, 3, 6, 8, 1, 5, 10]
print(isLevelOrderBST(arr1))  

arr2 = [11, 6, 13, 5, 12, 10]
print(isLevelOrderBST(arr2)) 
