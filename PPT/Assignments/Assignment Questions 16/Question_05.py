'''Given a number , write a program to reverse this number using stack.

**Examples:**
Input : 365
Output : 563

Input : 6899
Output : 9986'''

def reverseNumber(number):
    numberStr = str(number)
    stack = []

    # Push each character to the stack
    for char in numberStr:
        stack.append(char)

    reversedNumberStr = ""
    
    # Pop each character from the stack and append it to the reversed number string
    while len(stack) > 0:
        reversedNumberStr += stack.pop()

    reversedNumber = int(reversedNumberStr)
    return reversedNumber

# Example usage
number = 365
reversedNumber = reverseNumber(number)
print(reversedNumber)  # 563
