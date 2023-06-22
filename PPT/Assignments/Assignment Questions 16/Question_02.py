'''Given a stack of integers, sort it in ascending order using another temporary stack.

**Examples:**
Input : [34, 3, 31, 98, 92, 23]
Output : [3, 23, 31, 34, 92, 98]

'''
def sortStack(stack):
    tempStack = []

    while stack:
        temp = stack.pop()
        
        while tempStack and tempStack[-1] > temp:
            stack.append(tempStack.pop())

        tempStack.append(temp)

    # Reverse the temporary stack to get elements in ascending order
    tempStack.reverse()

    return tempStack

# Example usage
stack = [34, 3, 31, 98, 92, 23]
output = sortStack(stack)
print(output)  # [3, 23, 31, 34, 92, 98]

