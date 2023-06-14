'''Write a function that takes a list sorted in non-decreasing order and deletes any duplicate nodes from the list. The list should only be traversed once.

For example if the linked list is 11->11->11->21->43->43->60 then removeDuplicates() should convert the list to 11->21->43->60.

**Example 1:**
Input:
LinkedList: 
11->11->11->21->43->43->60
Output:
11->21->43->60

Example 2:
Input:
LinkedList: 
10->12->12->25->25->25->34
Output:
10->12->25->34'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeDuplicates(head):
    current = head

    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

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
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Example usage
list1 = createLinkedList([11, 11, 11, 21, 43, 43, 60])
list2 = createLinkedList([10, 12, 12, 25, 25, 25, 34])

newList1 = removeDuplicates(list1)
printLinkedList(newList1)  # Output: 11 21 43 60

newList2 = removeDuplicates(list2)
printLinkedList(newList2)  # Output: 10 12 25 34
