'''
💡 You are given a large integer represented as an integer array digits, where each
digits[i] is the ith digit of the integer. The digits are ordered from most significant
to least significant in left-to-right order. The large integer does not contain any
leading 0's.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**
Input: digits = [1,2,3]
Output: [1,2,4]

**Explanation:** The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

'''
def plusOne(digits):
    carry = 1
    n = len(digits)
    
    for i in range(n - 1, -1, -1):
        sum = digits[i] + carry
        if sum < 10:
            digits[i] = sum
            carry = 0
        else:
            digits[i] = sum % 10
            carry = 1
    
    if carry == 1:
        digits.insert(0, 1)
    
    return digits

# Test the function
digits = [1, 2, 3]
result = plusOne(digits)
print(result)