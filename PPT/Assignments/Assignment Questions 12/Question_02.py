'''Given a linked list of **N** nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.

**Example 1:**

```
Input:
N = 3
value[] = {1,3,4}
x(position at which tail is connected) = 2
Output:True
Explanation:In above test case N = 3.
The linked list with nodes N = 3 is
given. Then value of x=2 is given which
means last node is connected with xth
node of linked list. Therefore, there
exists a loop.
```

**Example 2:**
Input:
N = 4
value[] = {1,8,3,4}
x = 0
Output:False
Explanation:For N = 4 ,x = 0 means
then lastNode->next = NULL, then
the Linked list does not contains
any loop.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detectLoop(head):
    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            return True

    return False

# Example usage
# Create a linked list: 1->2->3->4->5->2 (forming a loop)
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next

# Check if the linked list contains a loop
has_loop = detectLoop(head)

if has_loop:
    print("The linked list contains a loop")
else:
    print("The linked list does not contain a loop")
