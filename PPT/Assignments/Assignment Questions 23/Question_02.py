'''Given a Binary tree, the task is to print the **left view** of the Binary Tree. The left view of a Binary Tree is a set of leftmost nodes for every level.

**Examples:**

***Input:***

            4

          /   \

        5     2

             /   \

            3     1

           /  \

          6    7

***Output:** 4 5 3 6*

**Explanation:**
***Input:***

                    1

                  /   \

                2       3

                 \

                   4

                     \

                        5

                           \

                             6

**Output:** 1 2 4 5 6'''
from collections import deque

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def printLeftView(root):
    if root is None:
        return
    
    queue = deque([(root, 0)])
    maxLevel = -1

    while queue:
        currentNode, level = queue.popleft()

        if level > maxLevel:
            print(currentNode.data, end=" ")
            maxLevel = level

        if currentNode.left:
            queue.append((currentNode.left, level + 1))
        if currentNode.right:
            queue.append((currentNode.right, level + 1))


# Create the binary tree
root = Node(4)
root.left = Node(5)
root.right = Node(2)
root.right.left = Node(3)
root.right.right = Node(1)
root.right.left.left = Node(6)
root.right.left.right = Node(7)

# Print the left view
print("Left View: ", end="")
printLeftView(root)

