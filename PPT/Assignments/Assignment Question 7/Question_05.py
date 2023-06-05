'''Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

**Example 1:**

**Input:** s = "abcdefg", k = 2

**Output:**

"bacdfeg"'''

def reverse_string(s, k):
    chars = list(s)
    for i in range(0, len(chars), 2 * k):
        chars[i:i + k] = reversed(chars[i:i + k])
    return ''.join(chars)
s = "abcdefg"
k = 2

reversed_string = reverse_string(s, k)
print(reversed_string)
