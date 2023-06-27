'''Given a Binary Search Tree with all unique values and two keys. Find the distance between two nodes in BST. The given keys always exist in BST.

Example:

Consider the following BST:
**Input-1:**

n = 9

values = [8, 3, 1, 6, 4, 7, 10, 14,13]

node-1 = 6

node-2 = 14

**Output-1:**

The distance between the two keys = 4

**Input-2:**

n = 9

values = [8, 3, 1, 6, 4, 7, 10, 14,13]

node-1 = 3

node-2 = 4

**Output-2:**

The distance between the two keys = 2'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findLCA(root, node1, node2):
    while root:
        if root.val > node1 and root.val > node2:
            root = root.left
        elif root.val < node1 and root.val < node2:
            root = root.right
        else:
            break

    return root

def findDistance(root, node, distance):
    if root.val == node:
        return distance

    if root.val > node:
        return findDistance(root.left, node, distance + 1)

    return findDistance(root.right, node, distance + 1)

def findDistanceBetweenNodes(root, node1, node2):
    lca = findLCA(root, node1, node2)

    distance1 = findDistance(lca, node1, 0)
    distance2 = findDistance(lca, node2, 0)

    return distance1 + distance2

# Example usage
root = TreeNode(8)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right = TreeNode(10)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

node1 = 6
node2 = 14

distance = findDistanceBetweenNodes(root, node1, node2)
print("The distance between the two keys:", distance)  

node1 = 3
node2 = 4

distance = findDistanceBetweenNodes(root, node1, node2)
print("The distance between the two keys:", distance)  
