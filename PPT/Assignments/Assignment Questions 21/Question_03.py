'''Write a program to convert a binary tree to a doubly linked list.

Input:

        10

       /   \

     5     20

           /   \

        30     35

Output:

5 10 30 20 35'''
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

def convertToDLL(root):
    # Static variable to store the previous node
    convertToDLL.prev = None

    def convertToDLLUtil(node):
        if node is None:
            return

        # Recursively convert the left subtree
        convertToDLLUtil(node.left)

        # Update the links
        if convertToDLL.prev:
            convertToDLL.prev.next = node
            node.prev = convertToDLL.prev
        else:
            # This is the leftmost node, set it as the head of the doubly linked list
            head = node

        convertToDLL.prev = node

        # Recursively convert the right subtree
        convertToDLLUtil(node.right)

    convertToDLLUtil(root)

    return head

# Example usage
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Construct the binary tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(30)
root.right.right = TreeNode(35)

# Convert the binary tree to doubly linked list
head = convertToDLL(root)

# Traverse the doubly linked list
current = head
while current:
    print(current.val, end=" ")
    current = current.next
