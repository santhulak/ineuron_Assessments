'''Given two non-negative integers, num1 and num2 represented as string, return *the sum of* num1 *and* num2 *as a string*.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

**Example 1:**

**Input:** num1 = "11", num2 = "123"

**Output:**

"134"'''

def add_strings(num1, num2):
    result = []
    carry = 0
    i = len(num1) - 1
    j = len(num2) - 1
    
    while i >= 0 or j >= 0 or carry > 0:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0
        total = digit1 + digit2 + carry
        digit = total % 10
        carry = total // 10
        result.append(str(digit))
        
        i -= 1
        j -= 1
    
    result.reverse()
    return ''.join(result)


num1 = "11"
num2 = "123"

result = add_strings(num1, num2)
print(result)
