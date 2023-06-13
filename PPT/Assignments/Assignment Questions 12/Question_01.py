'''
Given a singly linked list, delete **middle** of the linked list. For example, if given linked list is 1->2->**3**->4->5 then linked list should be modified to 1->2->4->5.If there are **even** nodes, then there would be **two middle** nodes, we need to delete the second middle element. For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.If the input linked list is NULL or has 1 node, then it should return NULL

**Example 1:**

```
Input:
LinkedList: 1->2->3->4->5
Output:1 2 4 5

```

**Example 2:**
Input:
LinkedList: 2->4->6->7->5->1
Output:2 4 6 5 1
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteMiddleNode(head):
    if head is None or head.next is None:
        return head

    slow_ptr = head
    fast_ptr = head
    prev_ptr = None

    while fast_ptr is not None and fast_ptr.next is not None:
        fast_ptr = fast_ptr.next.next
        prev_ptr = slow_ptr
        slow_ptr = slow_ptr.next

    prev_ptr.next = slow_ptr.next

    return head

# Example usage
# Create a linked list: 1->2->3->4->5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Print the original linked list
current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next
# Output: 1 2 3 4 5

print()

# Delete the middle node(s)
head = deleteMiddleNode(head)

# Print the modified linked list
current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next
# Output: 1 2 4 5
