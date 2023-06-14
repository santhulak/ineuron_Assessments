'''Given a **Doubly Linked List**, the task is to reverse the given Doubly Linked List.

**Example:**
Original Linked list 10 8 4 2
Reversed Linked list 2 4 8 10'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def reverseDoublyLinkedList(head):
    if head is None:
        return None

    current = head
    prev = None

    while current is not None:
        next = current.next
        current.next = prev
        current.prev = next
        prev = current
        current = next

    head = prev
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
doublyLinkedList = createDoublyLinkedList([10, 8, 4, 2])
reversedLinkedList = reverseDoublyLinkedList(doublyLinkedList)
printDoublyLinkedList(reversedLinkedList)  # Output: 2 4 8 10
