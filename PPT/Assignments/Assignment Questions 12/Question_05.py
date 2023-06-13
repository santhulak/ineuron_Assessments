'''Given a linked list of **N** nodes such that it may contain a loop.

A loop here means that the last node of the link list is connected to the node at position X(1-based index). If the link list does not have any loop, X=0.

Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.

**Example 1:**

```
Input:
N = 3
value[] = {1,3,4}
X = 2
Output:1
Explanation:The link list looks like
1 -> 3 -> 4
     ^    |
     |____|
A loop is present. If you remove it
successfully, the answer will be 1.

```

**Example 2:**
Input:
N = 4
value[] = {1,8,3,4}
X = 0
Output:1
Explanation:The Linked list does not
contains any loop.

Example 3:
Input:
N = 4
value[] = {1,2,3,4}
X = 1
Output:1
Explanation:The link list looks like
1 -> 2 -> 3 -> 4
^              |
|______________|
A loop is present.
If you remove it successfully,
the answer will be 1.'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detectAndRemoveLoop(head):
    slow_ptr = head
    fast_ptr = head

    # Detect the loop
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            break

    # If no loop is found, return
    if slow_ptr != fast_ptr:
        return

    # Move slow_ptr to the head and keep fast_ptr at the meeting point
    slow_ptr = head
    while slow_ptr.next != fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next

    # Remove the loop
    fast_ptr.next = None

# Example usage
# Create a linked list with a loop: 1 -> 3 -> 4 -> 2 -> 5 -> 6
head = Node(1)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(2)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = head.next.next

# Detect and remove the loop
detectAndRemoveLoop(head)

# Verify if the loop is removed
temp = head
visited = set()
while temp:
    if temp in visited:
        print("Loop is present")
        break
    visited.add(temp)
    temp = temp.next
else:
    print("Loop is not present")

# Print the modified linked list
temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next
