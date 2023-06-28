'''You are given a stack **St**. You have to reverse the stack using recursion.

**Example 1:**

```
Input:St = {3,2,1,7,6}
Output:{6,7,1,2,3}
```

**Example 2:**

```
Input:St = {4,3,9,6}
Output:{6,9,3,4}
```

'''

def reverseStack(stack):
    if len(stack) <= 1:
        return
    temp = stack.pop()
    reverseStack(stack)
    insertAtBottom(stack, temp)

def insertAtBottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
    else:
        temp = stack.pop()
        insertAtBottom(stack, item)
        stack.append(temp)

# Example usage
stack = [3, 2, 1, 7, 6]
print("Original stack:", stack)
reverseStack(stack)
print("Reversed stack:", stack)
