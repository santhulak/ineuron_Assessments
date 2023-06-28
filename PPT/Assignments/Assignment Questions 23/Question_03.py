'''

Given a Binary Tree, print the Right view of it.

The right view of a Binary Tree is a set of nodes visible when the tree is visited from the Right side.

**Examples:**

**Input:**

         1

      /     \

   2         3

/   \       /  \

4     5   6    7

             \

               8

**Output**: 

Right view of the tree is 1 3 7 8

**Input:**

         1

       /

    8

  /

7

**Output**: 

Right view of the tree is 1 8 7

'''
from collections import deque

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def printRightView(root):
    if root is None:
        return
    
    queue = deque([(root, 0)])
    maxLevel = -1

    while queue:
        currentNode, level = queue.popleft()

        if level > maxLevel:
            print(currentNode.data, end=" ")
            maxLevel = level

        if currentNode.right:
            queue.append((currentNode.right, level + 1))
        if currentNode.left:
            queue.append((currentNode.left, level + 1))


# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)

# Print the right view
print("Right View: ", end="")
printRightView(root)

