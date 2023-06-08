'''
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.
You always start to construct the **left** child node of the parent first if it exists.
**Input:** s = "4(2(3)(1))(6(5))"

**Output:** [4,2,6,3,1,5]
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(s):
    if not s:
        return None

    # Find the index of the first opening parenthesis
    idx = s.find('(')

    if idx == -1:
        # No opening parenthesis found, so the entire string represents a single node
        return TreeNode(int(s))

    # The value of the current node is the substring before the opening parenthesis
    val = int(s[:idx])

    # Find the index of the matching closing parenthesis for the current opening parenthesis
    count = 0
    for i in range(idx, len(s)):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            count -= 1

        if count == 0:
            break

    # Construct the left child tree by recursively calling the buildTree function
    left = buildTree(s[idx + 1:i])

    # Construct the right child tree by recursively calling the buildTree function
    right = buildTree(s[i + 2:-1])

    # Create the current node with the found value and constructed child trees
    node = TreeNode(val, left, right)

    return node

# Test the function
s = "4(2(3)(1))(6(5))"
root = buildTree(s)

# Function to flatten the binary tree into a list
def flattenTree(node):
    if not node:
        return []

    result = [node.val]
    result.extend(flattenTree(node.left))
    result.extend(flattenTree(node.right))

    return result

# Flatten the constructed binary tree into a list
result = flattenTree(root)
print(result)

