'''You are given a binary tree. The binary tree is represented using the TreeNode class. Each TreeNode has an integer value and left and right children, represented using the TreeNode class itself. Convert this binary tree into a binary search tree.

Input:

        10

       /   \

     2      7

   /   \

 8      4

Output:

        8

      /   \

    4     10

  /   \

2      7'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inOrderTraversal(root, values):
    if root is None:
        return
    
    inOrderTraversal(root.left, values)
    values.append(root.val)
    inOrderTraversal(root.right, values)

def constructBST(values, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    root = TreeNode(values[mid])
    
    root.left = constructBST(values, start, mid - 1)
    root.right = constructBST(values, mid + 1, end)
    
    return root

def convertToBST(root):
    values = []
    inOrderTraversal(root, values)
    values.sort()
    
    return constructBST(values, 0, len(values) - 1)

# Example usage
root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(8)
root.left.right = TreeNode(4)

bst_root = convertToBST(root)
print(bst_root.val) 
print(bst_root.left.val)  
print(bst_root.right.val)  
print(bst_root.left.left.val)  
print(bst_root.left.right.val)  
