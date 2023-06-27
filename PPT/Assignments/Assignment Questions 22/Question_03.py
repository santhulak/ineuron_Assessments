'''Given a binary tree, print all its root-to-leaf paths without using recursion. For example, consider the following Binary Tree.

Input:

        6
     /    \
    3      5
  /   \     \
 2     5     4
     /   \
    7     4

Output:

There are 4 leaves, hence 4 root to leaf paths -
  6->3->2
  6->3->5->7
  6->3->5->4
  6->5>4'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printRootToLeafPaths(root):
    if root is None:
        return

    stack = [(root, "")]
    while stack:
        node, path = stack.pop()

        if node.left is None and node.right is None:
            print(path + str(node.data))

        if node.right is not None:
            stack.append((node.right, path + str(node.data) + "->"))

        if node.left is not None:
            stack.append((node.left, path + str(node.data) + "->"))


# Create the binary tree
root = Node(6)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.right = Node(4)
root.left.right.left = Node(7)
root.left.right.right = Node(4)

print("Root-to-leaf Paths:")
printRootToLeafPaths(root)
