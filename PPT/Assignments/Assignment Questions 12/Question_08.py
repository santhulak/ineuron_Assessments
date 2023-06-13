'''Given a singly linked list, find if the linked list is [circular](https://www.geeksforgeeks.org/circular-linked-list/amp/) or not.

> A linked list is called circular if it is not NULL-terminated and all nodes are connected in the form of a cycle. Below is an example of a circular linked list.
>'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def isCircular(head):
    if head is None:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

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
arr = [1, 2, 3, 4, 5]
head = createLinkedList(arr)

# Make the linked list circular by connecting the last node to the head
temp = head
while temp.next:
    temp = temp.next
temp.next = head

# Check if the linked list is circular
if isCircular(head):
    print("The linked list is circular")
else:
    print("The linked list is not circular")
