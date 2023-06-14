'''
Given two sorted linked lists consisting of **N** and **M** nodes respectively. The task is to merge both of the lists (in place) and return the head of the merged list.

**Examples:**

Input: a: 5->10->15, b: 2->3->20

Output: 2->3->5->10->15->20

Input: a: 1->1, b: 2->4

Output: 1->1->2->4

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeSortedLists(a, b):
    dummy = Node(0)
    current = dummy

    while a is not None and b is not None:
        if a.data <= b.data:
            current.next = a
            a = a.next
        else:
            current.next = b
            b = b.next

        current = current.next

    if a is not None:
        current.next = a

    if b is not None:
        current.next = b

    return dummy.next

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
list1 = createLinkedList([5, 10, 15])
list2 = createLinkedList([2, 3, 20])
mergedList = mergeSortedLists(list1, list2)
printLinkedList(mergedList)  # Output: 2 3 5 10 15 20
