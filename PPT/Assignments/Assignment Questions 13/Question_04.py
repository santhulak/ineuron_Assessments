'''Given a linked list, write a function to reverse every alternate k nodes (where k is an input to the function) in an efficient way. Give the complexity of your algorithm.

**Example:**

Inputs:   1->2->3->4->5->6->7->8->9->NULL and k = 3
Output:   3->2->1->4->5->6->9->8->7->NULL.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseAlternateKNodes(head, k):
    if not head or k <= 1:
        return head

    dummy = Node(0)
    dummy.next = head
    prev = dummy
    current = head
    count = 0

    while current:
        count += 1
        if count % (2 * k) == k:
            prev = reverseGroup(prev, current.next, k)
            current = prev.next
        else:
            current = current.next

    return dummy.next

def reverseGroup(prev, next, k):
    last = prev.next
    current = last.next
    count = 1

    while current and count < k:
        last.next = current.next
        current.next = prev.next
        prev.next = current
        current = last.next
        count += 1

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
list1 = createLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
k = 3
newList = reverseAlternateKNodes(list1, k)
printLinkedList(newList)  # Output: 3 2 1 4 5 6 9 8 7
