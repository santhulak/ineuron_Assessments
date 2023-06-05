'''Given two strings s and t, return true *if they are equal when both are typed into empty text editors*. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

**Example 1:**

**Input:** s = "ab#c", t = "ad#c"

**Output:** true

**Explanation:**

Both s and t become "ac".'''
def process_backspaces(s):
    stack = []
    for char in s:
        if char != '#':
            stack.append(char)
        elif stack:
            stack.pop()
    return ''.join(stack)

def backspace_compare(s, t):
    processed_s = process_backspaces(s)
    processed_t = process_backspaces(t)
    return processed_s == processed_t

# Example usage
s = "ab#c"
t = "ad#c"
result = backspace_compare(s, t)
print(result)
