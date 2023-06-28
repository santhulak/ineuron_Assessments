'''Given string **S** representing a postfix expression, the task is to evaluate the expression and find the final value. Operators will only include the basic arithmetic operators like ***, /, + and -**.

**Example 1:**

```
Input: S = "231*+9-"
Output: -4
Explanation:
After solving the given expression,
we have -4 as result.

```

**Example 2:**

```
Input: S = "123+*8-"
Output: -3
Explanation:
After solving the given postfix
expression, we have -3 as result.
```

'''
def evaluatePostfixExpression(S):
    stack = []
    # Scan the expression
    for char in S:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = performOperation(char, operand1, operand2)
            stack.append(result)
    # Final result will be the top element of the stack
    return stack.pop()

def performOperation(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2

# Example usage
S = "231*+9-"
result = evaluatePostfixExpression(S)
print("Postfix Expression:", S)
print("Result:", result)
