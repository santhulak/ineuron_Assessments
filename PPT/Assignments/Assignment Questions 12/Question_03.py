'''
Given a linked list consisting of **L** nodes and given a number **N**. The task is to find the **N**th node from the end of the linked list.

**Example 1:**

```
Input:
N = 2
LinkedList: 1->2->3->4->5->6->7->8->9
Output:8
Explanation:In the first example, there
are 9 nodes in linked list and we need
to find 2nd node from end. 2nd node
from end is 8.

```

**Example 2:**

Input:
N = 5
LinkedList: 10->5->100->5
Output:-1
Explanation:In the second example, there
are 4 nodes in the linked list and we
need to find 5th from the end. Since 'n'
is more than the number of nodes in the
linked list, the output is -1.'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findNthFromEnd(head, N):
    mainPtr = head
    refPtr = head

    # Move refPtr N nodes ahead
    count = 0
    while count < N:
        if refPtr is None:
            return -1  # N is greater than the number of nodes
        refPtr = refPtr.next
        count += 1

    # Move both pointers until refPtr reaches the end
    while refPtr:
        mainPtr = mainPtr.next
        refPtr = refPtr.next

    # mainPtr will be pointing to the Nth node from the end
    return mainPtr.data

# Function to create a linked list from a given list
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

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
N = 2
head = createLinkedList(arr)

print("Linked list:")
temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next
print()

result = findNthFromEnd(head, N)
print("Nth node from the end:", result)

