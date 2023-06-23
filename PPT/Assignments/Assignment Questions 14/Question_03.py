'''Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:(i) a **next** pointer to the next node,(ii) a **bottom** pointer to a linked list where this node is head.Each of the sub-linked-list is in sorted order.Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. **Note:** The flattened list will be printed using the bottom pointer instead of next pointer.

**Example 1:**

```
Input:
5 -> 10 -> 19 -> 28
|     |     |     |
7     20    22   35
|           |     |
8          50    40
|                 |
30               45
Output: 5-> 7-> 8- > 10 -> 19-> 20->
22-> 28-> 30-> 35-> 40-> 45-> 50.
Explanation:
The resultant linked lists has every
node in a single level.(Note:| represents the bottom pointer.)

```

**Example 2:**
Input:
5 -> 10 -> 19 -> 28
|          |
7          22
|          |
8          50
|
30
Output: 5->7->8->10->19->22->28->30->50
Explanation:
The resultant linked lists has every
node in a single level.

(Note:| represents the bottom pointer.)'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.bottom = None

def mergeLists(a, b):
    if not a:
        return b
    if not b:
        return a
    
    result = None
    if a.val <= b.val:
        result = a
        result.bottom = mergeLists(a.bottom, b)
    else:
        result = b
        result.bottom = mergeLists(a, b.bottom)
    
    return result

def flatten(head):
    if not head or not head.next:
        return head
    
    head.bottom = flatten(head.bottom)
    head = mergeLists(head, head.next)
    
    return head

def printList(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.bottom

# Test case 1
head = ListNode(5)
head.next = ListNode(10)
head.next.next = ListNode(19)
head.next.next.next = ListNode(28)

head.bottom = ListNode(7)
head.bottom.bottom = ListNode(8)
head.bottom.bottom.bottom = ListNode(30)

head.next.bottom = ListNode(20)

head.next.next.bottom = ListNode(22)
head.next.next.next.bottom = ListNode(35)

head.next.next.next.bottom.bottom = ListNode(50)

head.next.next.next.next.bottom = ListNode(40)
head.next.next.next.next.bottom.bottom = ListNode(45)

head = flatten(head)
printList(head)
# Output: 5 7 8 10 19 20 22 28 30 35 40 45 50

# Test case 2
head = ListNode(5)
head.next = ListNode(10)
head.next.next = ListNode(19)
head.next.next.next = ListNode(28)

head.bottom = ListNode(7)
head.bottom.bottom = ListNode(22)

head.next.bottom = ListNode(8)

head.next.next.bottom = ListNode(50)

head.next.next.bottom.bottom = ListNode(30)

head = flatten(head)
printList(head)

