'''

Given a string `s`, *find the first non-repeating character in it and return its index*. If it does not exist, return `-1`.

**Example 1:**

```
Input: s = "leetcode"
Output: 0

```

**Example 2:**

```
Input: s = "loveleetcode"
Output: 2

```

**Example 3:**
Input: s = "aabb"
Output: -1
'''


def firstUniqChar(s):
    freq = {}
    
    # Count the frequency of each character
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    # Find the first character with frequency 1
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i
    
    return -1

# Example usage
s = "leetcode"
result = firstUniqChar(s)
print(result)  # Output: 0

s = "loveleetcode"
result = firstUniqChar(s)
print(result)  # Output: 2

s = "aabb"
result = firstUniqChar(s)
print(result)  # Output: -1
