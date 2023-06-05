'''Given two strings s and t, *determine if they are isomorphic*.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

**Example 1:**

**Input:** s = "egg", t = "add"

**Output:** true'''

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    # Create two dictionaries to store the mappings
    s_to_t = {}
    t_to_s = {}
    
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        
        # Check if the characters have been mapped before
        if char_s in s_to_t and s_to_t[char_s] != char_t:
            return False
        if char_t in t_to_s and t_to_s[char_t] != char_s:
            return False
        
        # Create the mappings
        s_to_t[char_s] = char_t
        t_to_s[char_t] = char_s
    
    return True

s = "egg"
t = "add"

result = is_isomorphic(s, t)
print(result)
