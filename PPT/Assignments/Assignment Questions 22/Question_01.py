'''Given a Binary Tree (Bt), convert it to a Doubly Linked List(DLL). The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be the same as in Inorder for the given Binary Tree. The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.

Example:
10
| 12 | 15
25 | 30 |36 
the above tree should be placed converted to the following double linked list
25 -> 12->30->10->36->15'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def convertToDLL(root):
    if root is None:
        return root

    # Convert the left subtree
    if root.left:
        left_head = convertToDLL(root.left)

        # Find the inorder predecessor (rightmost node) of the current node
        while left_head.right:
            left_head = left_head.right

        # Set the right pointer of the inorder predecessor to the current node
        left_head.right = root
        root.left = left_head

    # Convert the right subtree
    if root.right:
        right_head = convertToDLL(root.right)

        # Find the inorder successor (leftmost node) of the current node
        while right_head.left:
            right_head = right_head.left

        # Set the left pointer of the inorder successor to the current node
        right_head.left = root
        root.right = right_head

    return root


def printDLL(head):
    # Print the DLL starting from the head node
    current = head
    while current:
        print(current.data, end=" ")
        current = current.right
    print()


# Create the binary tree
root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)

# Convert the binary tree to DLL
head = convertToDLL(root)

# Print the DLL
printDLL(head)
