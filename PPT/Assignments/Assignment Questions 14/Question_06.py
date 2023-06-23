'''Given a singly linked list of size **N**. The task is to **left-shift** the linked list by **k** nodes, where **k** is a given positive integer smaller than or equal to length of the linked list.

**Example 1:**

```
Input:
N = 5
value[] = {2, 4, 7, 8, 9}
k = 3
Output:8 9 2 4 7
Explanation:Rotate 1:4 -> 7 -> 8 -> 9 -> 2
Rotate 2: 7 -> 8 -> 9 -> 2 -> 4
Rotate 3: 8 -> 9 -> 2 -> 4 -> 7

```

**Example 2:**
Input:
N = 8
value[] = {1, 2, 3, 4, 5, 6, 7, 8}
k = 4
Output:5 6 7 8 1 2 3 4'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateLeft(head, k):
    if not head or k == 0:
        return head

    length = 0
    current = head
    while current:
        length += 1
        if length == k + 1:
            newHead = current
        if not current.next:
            current.next = head
            break
        current = current.next

    tail = current

    for _ in range(length - k):
        tail = tail.next
        newHead = newHead.next

    tail.next = None

    return newHead

# Example 1
head = ListNode(2)
head.next = ListNode(4)
head.next.next = ListNode(7)
head.next.next.next = ListNode(8)
head.next.next.next.next = ListNode(9)
k = 3
rotated = rotateLeft(head, k)
while rotated:
    print(rotated.val, end=" ")  # Output: 8 9 2 4 7
    rotated = rotated.next
print()

# Example 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
k = 4
rotated = rotateLeft(head, k)
while rotated:
    print(rotated.val, end=" ")  # Output: 5 6 7 8 1 2 3 4
    rotated = rotated.next
print()
