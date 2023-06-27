'''Write a program to connect nodes at the same level.

Input:

        1

      /   \

    2      3

  /   \   /   \

4     5 6    7

Output:

1 → -1

2 → 3

3 → -1

4 → 5

5 → 6

6 → 7

7 → -1'''
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

def connectNodesAtSameLevel(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            if i < level_size - 1:
                node.next = queue[0]

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            if i == level_size - 1:
                node.next = None

def printConnections(root):
    if root is None:
        return

    current = root
    while current:
        print(current.val, end=" → ")

        if current.next is None:
            print("-1")
            current = current.left
        else:
            current = current.next

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

connectNodesAtSameLevel(root)
printConnections(root)
