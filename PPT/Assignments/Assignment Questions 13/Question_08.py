'''Given a doubly linked list and a position. The task is to delete a node from given position in a doubly linked list.

**Example 1:**

```
Input:
LinkedList = 1 <--> 3 <--> 4
x = 3
Output:1 3
Explanation:After deleting the node at
position 3 (position starts from 1),
the linked list will be now as 1->3.

```

**Example 2:**
Input:
LinkedList = 1 <--> 5 <--> 2 <--> 9
x = 1
Output:5 2 9'''

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def deleteNodeAtPosition(head, position):
    if head is None:
        return None

    if position == 1:
        newHead = head.next
        if newHead is not None:
            newHead.prev = None
        return newHead

    current = head
    currentPosition = 1

    while currentPosition < position and current is not None:
        current = current.next
        currentPosition += 1

    if current is None:
        return head

    prevNode = current.prev
    nextNode = current.next

    if prevNode is not None:
        prevNode.next = nextNode

    if nextNode is not None:
        nextNode.prev = prevNode

    return head

def createDoublyLinkedList(arr):
    if len(arr) == 0:
        return None

    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
        newNode = Node(arr[i])
        temp.next = newNode
        newNode.prev = temp
        temp = temp.next

    return head

def printDoublyLinkedList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Example usage
doublyLinkedList = createDoublyLinkedList([1, 3, 4])
position = 3
updatedList = deleteNodeAtPosition(doublyLinkedList, position)
printDoublyLinkedList(updatedList)  # Output: 1 3

doublyLinkedList = createDoublyLinkedList([1, 5, 2, 9])
position = 1
updatedList = deleteNodeAtPosition(doublyLinkedList, position)
printDoublyLinkedList(updatedList)  # Output: 5 2 9
