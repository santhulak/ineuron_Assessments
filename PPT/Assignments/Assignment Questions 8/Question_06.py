'''
Given two strings s and p, return *an array of all the start indices of* p*'s anagrams in* s. You may return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**

**Input:** s = "cbaebabacd", p = "abc"

**Output:** [0,6]

**Explanation:**

The substring with start index = 0 is "cba", which is an anagram of "abc".

The substring with start index = 6 is "bac", which is an anagram of "abc".
'''

from collections import Counter

def findAnagrams(s, p):
    result = []
    p_count = Counter(p)
    s_count = Counter(s[:len(p)])

    if s_count == p_count:
        result.append(0)

    for i in range(len(p), len(s)):
        if s_count[s[i - len(p)]] == 1:
            del s_count[s[i - len(p)]]
        else:
            s_count[s[i - len(p)]] -= 1

        s_count[s[i]] += 1

        if s_count == p_count:
            result.append(i - len(p) + 1)

    return result

# Test the function
s = "cbaebabacd"
p = "abc"
anagram_indices = findAnagrams(s, p)
print(anagram_indices)
