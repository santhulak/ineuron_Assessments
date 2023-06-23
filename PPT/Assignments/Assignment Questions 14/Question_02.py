'''A number **N** is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

**Example 1:**

```
Input:
LinkedList: 4->5->6
Output:457

```

**Example 2:**
Input:
LinkedList: 1->2->3
Output:124'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def addOne(head):
    # Reverse the linked list
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    head = prev

    # Add 1 to the linked list
    carry = 1
    prev = None
    curr = head
    while curr:
        curr.val += carry
        carry = curr.val // 10
        curr.val %= 10
        prev = curr
        curr = curr.next

    # If there is a remaining carry, append a new node
    if carry:
        prev.next = ListNode(carry)

    # Reverse the linked list again to restore the original order
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    head = prev

    return head
# Example 1
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(6)
result = addOne(head)
while result:
    print(result.val, end='')
    result = result.next

# Example 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
result = addOne(head)
while result:
    print(result.val, end='')
    result = result.next
