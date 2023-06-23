'''Given the `head` of a linked list, we repeatedly delete consecutive sequences of nodes that sum to `0` until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of `ListNode` objects.)

**Example 1:**

```
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.

```

**Example 2:**

```
Input: head = [1,2,3,-3,4]
Output: [1,2,4]

```

**Example 3:**
Input: head = [1,2,3,-3,-2]
Output: [1]'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head):
    dummy = ListNode(0)
    dummy.next = head

    curr = dummy
    running_sum = 0
    sum_dict = {}

    while curr:
        running_sum += curr.val

        if running_sum in sum_dict:
            curr.next = sum_dict[running_sum].next
        else:
            sum_dict[running_sum] = curr

        curr = curr.next

    return dummy.next

# Example 1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(-3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(1)
result = removeZeroSumSublists(head)
while result:
    print(result.val, end=" ")
    result = result.next
# Output: 3 1

# Example 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(-3)
head.next.next.next.next = ListNode(4)
result = removeZeroSumSublists(head)
while result:
    print(result.val, end=" ")
    result = result.next
# Output: 1 2 4

# Example 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(-3)
head.next.next.next.next = ListNode(-2)
result = removeZeroSumSublists(head)
while result:
    print(result.val, end=" ")
    result = result.next
# Output: 1
