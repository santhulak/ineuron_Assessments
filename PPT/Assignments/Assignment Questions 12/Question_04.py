'''Given a singly linked list of characters, write a function that returns true if the given list is a palindrome, else false.
**Examples:**

> Input: R->A->D->A->R->NULL
> 
> 
> **Output:** Yes
> 
> **Input:** C->O->D->E->NULL
> 
> **Output:** No
>'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseList(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def isPalindrome(head):
    # Find the middle node
    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    # Reverse the second half of the list
    second_half = reverseList(slow_ptr)
    first_half = head

    # Compare the first half with the reversed second half
    while second_half is not None:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True

# Example usage
# Create a linked list: R->A->D->A->R->NULL
head = Node('R')
head.next = Node('A')
head.next.next = Node('D')
head.next.next.next = Node('A')
head.next.next.next.next = Node('R')

# Check if the linked list is a palindrome
is_palindrome = isPalindrome(head)

if is_palindrome:
    print("Yes, the linked list is a palindrome")
else:
    print("No, the linked list is not a palindrome")
