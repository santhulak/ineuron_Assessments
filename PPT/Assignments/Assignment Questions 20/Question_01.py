'''Given a binary tree, your task is to find subtree with maximum sum in tree.

Examples:

Input1 :       

       1

     /   \

   2      3

  / \    / \

4   5  6   7

Output1 : 28

As all the tree elements are positive, the largest subtree sum is equal to sum of all tree elements.

Input2 :

       1

     /    \

  -2      3

  / \    /  \

4   5  -6   2

Output2 : 7

Subtree with largest sum is :

 -2

 / \

4   5

Also, entire tree sum is also 7.

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxSubtreeSum(root):
    global max_sum
    max_sum = float('-inf')

    def computeSubtreeSum(node):
        global max_sum
        if node is None:
            return 0

        left_sum = computeSubtreeSum(node.left)
        right_sum = computeSubtreeSum(node.right)
        subtree_sum = node.val + left_sum + right_sum

        max_sum = max(max_sum, subtree_sum)

        return subtree_sum

    computeSubtreeSum(root)
    return max_sum

# Example 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(maxSubtreeSum(root))


# Example 2
root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(-6)
root.right.right = TreeNode(2)
print(maxSubtreeSum(root))

