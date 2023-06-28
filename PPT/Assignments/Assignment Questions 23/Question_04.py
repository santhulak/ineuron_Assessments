'''Given a Binary Tree, The task is to print the **bottom view** from left to right. A node **x** is there in output if x is the bottommost node at its horizontal distance. The horizontal distance of the left child of a node x is equal to a horizontal distance of x minus 1, and that of a right child is the horizontal distance of x plus 1.

**Examples:**

**Input:**

             20

           /     \

        8         22

    /      \         \

5         3        25

        /    \

   10       14

**Output:** 5, 10, 3, 14, 25.

**Input:**

             20

           /     \

        8         22

    /      \      /   \

 5         3    4     25

         /    \

     10       14

**Output:**

5 10 4 14 25.

**Explanation:**

If there are multiple bottom-most nodes for a horizontal distance from the root, then print the later one in the level traversal.

**3 and 4** are both the bottom-most nodes at a horizontal distance of 0, we need to print 4.'''
from collections import deque

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def printBottomView(root):
    if root is None:
        return

    # Create a hash map to store node values based on horizontal distance
    # The key is the horizontal distance, and the value is the node value
    hashMap = {}

    # Create a queue for level order traversal
    queue = deque([(root, 0)])

    # Perform level order traversal
    while queue:
        currentNode, hd = queue.popleft()

        # Update the node value in the hash map for the current horizontal distance
        hashMap[hd] = currentNode.data

        # Enqueue the left and right children of the current node
        if currentNode.left:
            queue.append((currentNode.left, hd - 1))
        if currentNode.right:
            queue.append((currentNode.right, hd + 1))

    # Print the bottom view values in the order of their horizontal distance
    for value in sorted(hashMap.keys()):
        print(hashMap[value], end=" ")


# Create the binary tree
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

# Print the bottom view
print("Bottom View: ", end="")
printBottomView(root)
