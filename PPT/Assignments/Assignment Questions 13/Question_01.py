'''
Given two linked list of the same size, the task is to create a new linked list using those linked lists. The condition is that the greater node among both linked list will be added to the new linked list.

**Examples:**
Input: list1 = 5->2->3->8
list2 = 1->7->4->5
Output: New list = 5->7->4->8

Input:list1 = 2->8->9->3
list2 = 5->3->6->4
Output: New list = 5->8->9->4
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeLinkedLists(list1, list2):
    head1 = list1
    head2 = list2
    newHead = None
    tail = None

    while head1 and head2:
        if head1.data >= head2.data:
            newNode = Node(head1.data)
            head1 = head1.next
        else:
            newNode = Node(head2.data)
            head2 = head2.next

        if newHead is None:
            newHead = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = tail.next

    # Append remaining nodes of list1 or list2
    if head1:
        tail.next = head1
    elif head2:
        tail.next = head2

    return newHead

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
list1 = createLinkedList([5, 2, 3, 8])
list2 = createLinkedList([1, 7, 4, 5])
newList = mergeLinkedLists(list1, list2)
printLinkedList(newList)  # Output: 5 7 4 8

list3 = createLinkedList([2, 8, 9, 3])
list4 = createLinkedList([5, 3, 6, 4])
newList2 = mergeLinkedLists(list3, list4)
printLinkedList(newList2)  # Output: 5 8 9 4
