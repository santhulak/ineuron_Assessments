'''Given Preorder, Inorder and Postorder traversals of some tree. Write a program to check if they all are of the same tree.

**Examples:**

Input : 

        Inorder -> 4 2 5 1 3
        Preorder -> 1 2 4 5 3
        Postorder -> 4 5 2 3 1
Output : 

Yes
Explanation : 

All of the above three traversals are of
the same tree 

                           1
                         /   \
                        2     3
                      /   \
                     4     5

Input : 

        Inorder -> 4 2 5 1 3
        Preorder -> 1 5 4 2 3
        Postorder -> 4 1 2 3 5
Output : 

No'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructTree(inorder, preorder):
    if not inorder or not preorder:
        return None

    root_data = preorder[0]
    root = Node(root_data)

    root_index = inorder.index(root_data)

    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]

    left_preorder = preorder[1:1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder):]

    root.left = constructTree(left_inorder, left_preorder)
    root.right = constructTree(right_inorder, right_preorder)

    return root


def isSameTree(inorder, preorder, postorder):
    constructed_tree = constructTree(inorder, preorder)

    def postorderTraversal(root):
        if root:
            postorderTraversal(root.left)
            postorderTraversal(root.right)
            postorder.append(root.data)

    postorder = []
    postorderTraversal(constructed_tree)

    return postorder == postorder


# Example 1:
inorder1 = [4, 2, 5, 1, 3]
preorder1 = [1, 2, 4, 5, 3]
postorder1 = [4, 5, 2, 3, 1]

if isSameTree(inorder1, preorder1, postorder1):
    print("Yes")
else:
    print("No")

# Example 2:
inorder2 = [4, 2, 5, 1, 3]
preorder2 = [1, 5, 4, 2, 3]
postorder2 = [4, 1, 2, 3, 5]

if isSameTree(inorder2, preorder2, postorder2):
    print("Yes")
else:
    print("No")
