'''Given a linked list and a key to be deleted. Delete last occurrence of key from linked. The list may have duplicates.

**Examples**:
Input:   1->2->3->5->2->10, key = 2
Output:  1->2->3->5->10'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteLastOccurrence(head, key):
    if not head:
        return None

    prev = None
    last = None
    temp = head

    while temp:
        if temp.data == key:
            prev = last
            last = temp

        temp = temp.next

    if last is None:
        return head

    if last == head:
        head = head.next
    else:
        prev.next = last.next

    del last

    return head

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
list1 = createLinkedList([1, 2, 3, 5, 2, 10])
key = 2
newList = deleteLastOccurrence(list1, key)
printLinkedList(newList)  # Output: 1 2 3 5 10
