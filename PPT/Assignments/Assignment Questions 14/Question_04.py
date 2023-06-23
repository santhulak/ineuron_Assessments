'''

You are given a special linked list with **N** nodes where each node has a next pointer pointing to its next node. You are also given **M** random pointers, where you will be given **M** number of pairs denoting two nodes **a** and **b**  **i.e. a->arb = b** (arb is pointer to random node)**.**

Construct a copy of the given list. The copy should consist of exactly **N** new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes **X** and **Y** in the original list, where **X.arb** **-->** **Y**, then for the corresponding two nodes **x** and **y** in the copied list, **x.arb --> y.**

Return the head of the copied linked list.
**Note** :- The diagram isn't part of any example, it just depicts an example of how the linked list may look like.

**Example 1:**

```
Input:
N = 4, M = 2
value = {1,2,3,4}
pairs = {{1,2},{2,4}}
Output:1
Explanation:In this test case, there
are 4 nodes in linked list.  Among these
4 nodes,  2 nodes have arbitrary pointer
set, rest two nodes have arbitrary pointer
as NULL. Second line tells us the value
of four nodes. The third line gives the
information about arbitrary pointers.
The first node arbitrary pointer is set to
node 2.  The second node arbitrary pointer
is set to node 4.

```

**Example 2:**
Input:
N = 4, M = 2
value[] = {1,3,5,9}
pairs[] = {{1,1},{3,4}}
Output:1
Explanation:In the given testcase ,
applying the method as stated in the
above example, the output will be 1.

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def copyRandomList(head):
    if not head:
        return None

    # Step 1: Create a deep copy of each node and insert it next to the original node
    current = head
    while current:
        new_node = Node(current.data)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next

    # Step 2: Set the random pointers of the new nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: Separate the original and copied lists
    current = head
    new_head = head.next
    while current:
        new_node = current.next
        current.next = new_node.next
        if new_node.next:
            new_node.next = new_node.next.next
        current = current.next

    # Step 4: Return the head of the copied list
    return new_head

# Example 1
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4
node1.random = node2
node2.random = node4

new_head = copyRandomList(node1)
current = new_head
while current:
    print("Node data:", current.data)
    if current.random:
        print("Random pointer:", current.random.data)
    else:
        print("Random pointer: None")
    current = current.next


# Example 2
node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(9)
node1.next = node2
node2.next = node3
node3.next = node4
node1.random = node1
node2.random = node4

new_head = copyRandomList(node1)
current = new_head
while current:
    print("Node data:", current.data)
    if current.random:
        print("Random pointer:", current.random.data)
    else:
        print("Random pointer: None")
    current = current.next

