'''A Given a binary tree, the task is to flip the binary tree towards the right direction that is clockwise. See the below examples to see the transformation.

In the flip operation, the leftmost node becomes the root of the flipped tree and its parent becomes its right child and the right sibling becomes its left child and the same should be done for all left most nodes recursively.

Example1:
1->2->3->4->5->6->7
4->5->2->3->1->6->7
Example2:
1->2->3->4->5
2->3->1->4->5
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def flipBinaryTree(root):
    if root is None or (root.left is None and root.right is None):
        return root

    flipped_left = flipBinaryTree(root.left)
    flipped_right = flipBinaryTree(root.right)

    root.left = flipped_right
    root.right = flipped_left

    return root


def inorderTraversal(root):
    if root is None:
        return

    inorderTraversal(root.left)
    print(root.data, end=" ")
    inorderTraversal(root.right)


# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Original Binary Tree:")
inorderTraversal(root)

# Flip the binary tree
flipped_root = flipBinaryTree(root)

print("\nFlipped Binary Tree:")
inorderTraversal(flipped_root)
