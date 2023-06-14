'''Given a linked list of size **N**. The task is to reverse every **k** nodes (where k is an input to the function) in the linked list. If the number of nodes is not a multiple of *k* then left-out nodes, in the end, should be considered as a group and must be reversed (See Example 2 for clarification).

**Example 1:**

```
Input:
LinkedList: 1->2->2->4->5->6->7->8
K = 4
Output:4 2 2 1 8 7 6 5
Explanation:
The first 4 elements 1,2,2,4 are reversed first
and then the next 4 elements 5,6,7,8. Hence, the
resultant linked list is 4->2->2->1->8->7->6->5.

```

**Example 2:**
Input:
LinkedList: 1->2->3->4->5
K = 3
Output:3 2 1 5 4
Explanation:
The first 3 elements are 1,2,3 are reversed
first and then elements 4,5 are reversed.Hence,
the resultant linked list is 3->2->1->5->4.'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseKNodes(head, k):
    if not head or k == 1:
        return head

    dummy = Node(0)
    dummy.next = head
    prev = dummy
    current = head
    count = 0

    while current:
        count += 1
        if count % k == 0:
            prev = reverseGroup(prev, current.next)
            current = prev.next
        else:
            current = current.next

    return dummy.next

def reverseGroup(prev, next):
    last = prev.next
    current = last.next

    while current != next:
        last.next = current.next
        current.next = prev.next
        prev.next = current
        current = last.next

    return last

def createLinkedList(arr):
    if len(arr) == 0:
        return None

    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
        newNode = Node(arr[i])
        temp.next = newNode
        temp = temp.next

    return head

def printLinkedList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Example usage
list1 = createLinkedList([1, 2, 2, 4, 5, 6, 7, 8])
k1 = 4
newList1 = reverseKNodes(list1, k1)
printLinkedList(newList1)  # Output: 4 2 2 1 8 7 6 5

list2 = createLinkedList([1, 2, 3, 4, 5])
k2 = 3
newList2 = reverseKNodes(list2, k2)
printLinkedList(newList2)  # Output: 3 2 1 5 4
