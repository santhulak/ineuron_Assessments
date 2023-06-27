'''Construct the BST (Binary Search Tree) from its given level order traversal.

Example:

Input: arr[] = {7, 4, 12, 3, 6, 8, 1, 5, 10}

Output: BST:

            7

         /    \

       4     12

     /  \     /

    3   6  8

   /    /     \

 1    5      10'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructBST(arr, start, end):
    if start > end:
        return None

    root = TreeNode(arr[start])

    # Find the index of the first element greater than the current node's value
    i = start + 1
    while i <= end and arr[i] <= root.val:
        i += 1

    # Construct left and right subtrees recursively
    root.left = constructBST(arr, start + 1, i - 1)
    root.right = constructBST(arr, i, end)

    return root

def inorderTraversal(root):
    if root is None:
        return []

    result = []
    result.extend(inorderTraversal(root.left))
    result.append(root.val)
    result.extend(inorderTraversal(root.right))
    return result

# Example usage
arr = [7, 4, 12, 3, 6, 8, 1, 5, 10]
root = constructBST(arr, 0, len(arr) - 1)
inorder = inorderTraversal(root)
print("BST:")
print(" ".join(str(val) for val in inorder))
