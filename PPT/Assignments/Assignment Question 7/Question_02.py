'''Given a string num which represents an integer, return true *if* num *is a **strobogrammatic number***.

A **strobogrammatic number** is a number that looks the same when rotated 180 degrees (looked at upside down).

**Example 1:**

**Input:** num = "69"

**Output:**

true'''

def is_strobogrammatic(num):
    valid_pairs = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    left, right = 0, len(num) - 1
    
    while left <= right:
        if num[left] not in valid_pairs or num[right] not in valid_pairs:
            return False
        if valid_pairs[num[left]] != num[right]:
            return False
        left += 1
        right -= 1
    
    return True
num = "69"

result = is_strobogrammatic(num)
print(result)
