'''Given preorder of a binary tree, calculate its **[depth(or height)](https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/)** [starting from depth 0]. The preorder is given as a string with two possible characters.

1. ‘l’ denotes the leaf
2. ‘n’ denotes internal node

The given tree can be seen as a full binary tree where every node has 0 or two children. The two children of a node can ‘n’ or ‘l’ or mix of both.

**Examples :**

Input  : nlnll
Output : 2
Explanation :
Input  : nlnnlll
Output : 3'''
def calculateDepth(preorder):
    depth = 0
    maxDepth = 0

    for char in preorder:
        if char == 'n':
            depth += 1
        elif char == 'l':
            maxDepth = max(maxDepth, depth)
            depth -= 1

    return maxDepth


# Example 1:
preorder1 = "nlnll"
depth1 = calculateDepth(preorder1)
print("Depth:", depth1)

# Example 2:
preorder2 = "nlnnlll"
depth2 = calculateDepth(preorder2)
print("Depth:", depth2)
