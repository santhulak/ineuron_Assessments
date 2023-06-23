'''You are given the `head` of a linked list with `n` nodes.

For each node in the list, find the value of the **next greater node**. That is, for each node, find the value of the first node that is next to it and has a **strictly larger** value than it.

Return an integer array `answer` where `answer[i]` is the value of the next greater node of the `ith` node (**1-indexed**). If the `ith` node does not have a next greater node, set `answer[i] = 0`.

**Example 1:**
Input: head = [2,1,5]
Output: [5,5,0]
Example 2:
Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nextLargerNodes(head):
    stack = []
    result = []
    current = head
    while current:
        while stack and stack[-1][0] < current.val:
            _, idx = stack.pop()
            result[idx] = current.val
        stack.append((current.val, len(result)))
        result.append(0)
        current = current.next
    return result[::-1]

# Example 1
head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(5)
result = nextLargerNodes(head)
print(result)  

# Example 2
head = ListNode(2)
head.next = ListNode(7)
head.next.next = ListNode(4)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)
result = nextLargerNodes(head)
print(result)  