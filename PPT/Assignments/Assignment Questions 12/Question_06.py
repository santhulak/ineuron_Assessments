'''Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes, continue the same till end of the linked list.

Difficulty Level: Rookie

**Examples**:
Input:
M = 2, N = 2
Linked List: 1->2->3->4->5->6->7->8
Output:
Linked List: 1->2->5->6

Input:
M = 3, N = 2
Linked List: 1->2->3->4->5->6->7->8->9->10
Output:
Linked List: 1->2->3->6->7->8

Input:
M = 1, N = 1
Linked List: 1->2->3->4->5->6->7->8->9->10
Output:
Linked List: 1->3->5->7->9'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def retainAndDelete(head, M, N):
    if M == 0:  # If M is 0, delete all nodes
        return None

    currPtr = head
    prevPtr = None

    while currPtr:
        # Skip M nodes
        for _ in range(M):
            if currPtr:
                prevPtr = currPtr
                currPtr = currPtr.next
            else:
                break

        # Delete N nodes
        for _ in range(N):
            if currPtr:
                currPtr = currPtr.next
            else:
                break

        # Update the next pointer of prevPtr
        prevPtr.next = currPtr

    return head

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

# Function to print a linked list
def printLinkedList(head):
    if head is None:
        print("Linked List: Empty")
        return

    temp = head
    linkedListStr = ""
    while temp:
        linkedListStr += str(temp.data) + "->"
        temp = temp.next
    linkedListStr += "None"
    print("Linked List:", linkedListStr)

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8]
M = 2
N = 2

head = createLinkedList(arr)
print("Original Linked List:")
printLinkedList(head)

modifiedHead = retainAndDelete(head, M, N)
print("Modified Linked List:")
printLinkedList(modifiedHead)
