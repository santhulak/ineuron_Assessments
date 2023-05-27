'''
💡 You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**
Input: digits = [1,2,3]
Output: [1,2,4]

**Explanation:** The array represents the integer 123.

Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

'''
def plusOne(digits):
    n = len(digits)
    carry = 1

    # Iterate through the digits from right to left
    for i in range(n - 1, -1, -1):
        digits[i] += carry

        if digits[i] < 10:
            carry = 0
            break

        digits[i] = 0

    # If there is still a carry, insert it at the beginning
    if carry == 1:
        digits.insert(0, carry)

    return digits

# Test the function
digits = [1, 2, 3]
result = plusOne(digits)
print(result)
