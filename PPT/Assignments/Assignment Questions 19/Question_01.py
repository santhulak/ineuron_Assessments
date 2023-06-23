'''

💡 **Merge k Sorted Lists**

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*

**Example 1:**

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

```

**Example 2:**
**Example 3:**

```
Input: lists = [[]]
Output: []

```

**Constraints:**

- `k == lists.length`
- `0 <= k <= 10000`
- `0 <= lists[i].length <= 500`
- `-10000 <= lists[i][j] <= 10000`
- `lists[i]` is sorted in **ascending order**.
- The sum of `lists[i].length` will not exceed `10000`.
'''

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []
    
    # Add the first node from each list to the min-heap
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i))
            lists[i] = lists[i].next

    dummy = ListNode()
    curr = dummy

    while heap:
        val, i = heapq.heappop(heap)
        curr.next = ListNode(val)
        curr = curr.next

        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i))
            lists[i] = lists[i].next

    return dummy.next


# Create the linked lists
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)

# Merge the linked lists
lists = [list1, list2, list3]
merged_list = mergeKLists(lists)

# Print the merged sorted linked list
while merged_list:
    print(merged_list.val, end=' ')
    merged_list = merged_list.next

