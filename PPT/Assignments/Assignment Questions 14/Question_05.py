'''Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return *the reordered list*.

The **first** node is considered **odd**, and the **second** node is **even**, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

**Example 1:**
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    if not head or not head.next:
        return head

    oddHead = head
    evenHead = head.next
    odd = oddHead
    even = evenHead

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = evenHead
    even.next = None

    return oddHead

# Example 1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
reordered = oddEvenList(head)
while reordered:
    print(reordered.val, end=" ")  # Output: 1 3 5 2 4
    reordered = reordered.next
print()

# Example 2
head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(6)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(7)
reordered = oddEvenList(head)
while reordered:
    print(reordered.val, end=" ")  # Output: 2 3 6 7 1 5 4
    reordered = reordered.next
print()
