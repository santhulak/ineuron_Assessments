'''Given a Queue consisting of first **n** natural numbers (in random order). The task is to check whether the given Queue elements can be arranged in increasing order in another Queue using a stack. The operation allowed are:

1. Push and pop elements from the stack
2. Pop (Or Dequeue) from the given Queue.
3. Push (Or Enqueue) in the another Queue.

**Examples :**

Input : Queue[] = { 5, 1, 2, 3, 4 } 

Output : Yes 

Pop the first element of the given Queue 

i.e 5. Push 5 into the stack. 

Now, pop all the elements of the given Queue and push them to second Queue. 

Now, pop element 5 in the stack and push it to the second Queue.
Given a Queue consisting of first **n** natural numbers (in random order). The task is to check whether the given Queue elements can be arranged in increasing order in another Queue using a stack. The operation allowed are:

1. Push and pop elements from the stack
2. Pop (Or Dequeue) from the given Queue.
3. Push (Or Enqueue) in the another Queue.

**Examples :**

Input : Queue[] = { 5, 1, 2, 3, 4 } 

Output : Yes 

Pop the first element of the given Queue 

i.e 5. Push 5 into the stack. 

Now, pop all the elements of the given Queue and push them to second Queue. 

Now, pop element 5 in the stack and push it to the second Queue.'''

from queue import Queue

def checkArrangement(queue):
    stack = []
    secondQueue = Queue()
    expectedElement = 1

    while not queue.empty():
        currentElement = queue.get()

        if currentElement == expectedElement:
            secondQueue.put(currentElement)
            expectedElement += 1
        else:
            if len(stack) > 0 and stack[-1] == expectedElement:
                stack.pop()
                secondQueue.put(expectedElement)
                expectedElement += 1
            else:
                stack.append(currentElement)

    while len(stack) > 0:
        if stack.pop() == expectedElement:
            secondQueue.put(expectedElement)
            expectedElement += 1
        else:
            return "No"

    return "Yes"

# Example usage
queue = Queue()
queue.put(5)
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)

result = checkArrangement(queue)
print(result)  # Yes
