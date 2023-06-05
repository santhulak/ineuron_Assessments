'''Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

**Example 1:**

**Input:** s = "Let's take LeetCode contest"

**Output:** "s'teL ekat edoCteeL tsetnoc"'''

def reverse_words(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

s = "Let's take LeetCode contest"

reversed_sentence = reverse_words(s)
print(reversed_sentence)
