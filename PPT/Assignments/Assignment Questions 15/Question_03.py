'''Implement a Stack using two queues **q1** and **q2**.

**Example 1:**

```
Input:
push(2)
push(3)
pop()
push(4)
pop()
Output:3 4
Explanation:
push(2) the stack will be {2}
push(3) the stack will be {2 3}
pop()   poped element will be 3 the
        stack will be {2}
push(4) the stack will be {2 4}
pop()   poped element will be 4

```

**Example 2:**

```
Input:
push(2)
pop()
pop()
push(3)
Output:2 -1
```



'''
class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, val):
        self.q1.append(val)

    def pop(self):
        if not self.isEmpty():
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            return self.q1.pop(0)
        return -1

    def top(self):
        if not self.isEmpty():
            return self.q1[-1]
        return -1

    def isEmpty(self):
        return len(self.q1) == 0 and len(self.q2) == 0


# Example usage
stack = Stack()
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
stack.push(4)
print(stack.pop())  # Output: 4
