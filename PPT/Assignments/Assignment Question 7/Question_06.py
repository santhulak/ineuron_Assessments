'''Given two strings s and goal, return true *if and only if* s *can become* goal *after some number of **shifts** on* s.

A **shift** on s consists of moving the leftmost character of s to the rightmost position.

- For example, if s = "abcde", then it will be "bcdea" after one shift.

**Example 1:**

**Input:** s = "abcde", goal = "cdeab"

**Output:**

true'''

def can_shift_string(s, goal):
    if len(s) != len(goal):
        return False
    return goal in (s + s)

# Example usage
s = "abcde"
goal = "cdeab"
result = can_shift_string(s, goal)
print(result)
