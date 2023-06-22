'''Given an integer k and a **[queue](https://www.geeksforgeeks.org/queue-data-structure/)** of integers, The task is to reverse the order of the first **k** elements of the queue, leaving the other elements in the same relative order.

Only following standard operations are allowed on queue.

- **enqueue(x) :** Add an item x to rear of queue
- **dequeue() :** Remove an item from front of queue
- **size() :** Returns number of elements in queue.
- **front() :** Finds front item.'''
from queue import Queue

def reverseKElements(queue, k):
    stack = []
    
    # Step 1: Dequeue the first k elements and push them onto the stack
    for i in range(k):
        stack.append(queue.get())
    
    # Step 2: Enqueue the elements from the stack back into the queue
    while stack:
        queue.put(stack.pop())
    
    # Step 3: Dequeue the remaining elements and enqueue them back into the queue
    for i in range(queue.qsize() - k):
        queue.put(queue.get())

# Example usage
queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)

k = 3
reverseKElements(queue, k)

# Printing the modified queue
while not queue.empty():
    print(queue.get(), end=" ")  # Output: 3 2 1 4 5
