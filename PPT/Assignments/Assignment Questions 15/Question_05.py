'''You are given a string **S**, the task is to reverse the string using stack.

**Example 1:**

```
Input: S="GeeksforGeeks"
Output: skeeGrofskeeG
```

'''
def reverseString(s):
    stack = []
    reversed_string = ""
    # Push each character onto the stack
    for char in s:
        stack.append(char)
    # Pop each character from the stack and append it to the reversed string
    while len(stack) > 0:
        reversed_string += stack.pop()
    return reversed_string

# Example usage
s = "GeeksforGeeks"
reversed_s = reverseString(s)
print("Original string:", s)
print("Reversed string:", reversed_s)
