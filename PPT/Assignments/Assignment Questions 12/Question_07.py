'''Given two linked lists, insert nodes of second list into first list at alternate positions of first list.
For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6, the first list should become 5->12->7->10->17->2->13->4->11->6 and second list should become empty. The nodes of second list should only be inserted when there are positions available. For example, if the first list is 1->2->3 and second list is 4->5->6->7->8, then first list should become 1->4->2->5->3->6 and second list to 7->8.

Use of extra space is not allowed (Not allowed to create additional nodes), i.e., insertion must be done in-place. Expected time complexity is O(n) where n is number of nodes in first list.'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAlternatePositions(first, second):
    if first is None:
        return second

    if second is None:
        return first

    firstPtr = first
    secondPtr = second

    while firstPtr and secondPtr:
        nextFirst = firstPtr.next
        nextSecond = secondPtr.next

        # Insert the node from the second list into the first list
        firstPtr.next = secondPtr
        secondPtr.next = nextFirst

        # Move the pointers
        firstPtr = nextFirst
        secondPtr = nextSecond

    if secondPtr:
        # Append the remaining nodes in the second list at the end of the first list
        firstPtr.next = secondPtr

    return first

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
arr1 = [5, 7, 17, 13, 11]
arr2 = [12, 10, 2, 4, 6]

head1 = createLinkedList(arr1)
head2 = createLinkedList(arr2)

print("Original First Linked List:")
printLinkedList(head1)
print("Original Second Linked List:")
printLinkedList(head2)

mergedHead = insertAlternatePositions(head1, head2)

print("Modified First Linked List:")
printLinkedList(mergedHead)
print("Modified Second Linked List:")
printLinkedList(head2)
