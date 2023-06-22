'''Given a stack with **push()**, **pop()**, and **empty()** operations, The task is to delete the **middle** element ****of it without using any additional data structure.

Input  : Stack[] = [1, 2, 3, 4, 5]

Output : Stack[] = [1, 2, 4, 5]

Input  : Stack[] = [1, 2, 3, 4, 5, 6]

Output : Stack[] = [1, 2, 4, 5, 6]'''

def deleteMiddle(stack, curr_index, mid_index):
    if len(stack) == 0:
        return
    
    item = stack.pop()
    
    deleteMiddle(stack, curr_index + 1, mid_index)
    
    if curr_index != mid_index:
        stack.append(item)

def deleteMiddleElement(stack):
    size = len(stack)
    mid_index = size // 2 if size % 2 == 1 else (size // 2) - 1
    
    deleteMiddle(stack, 0, mid_index)
    
    return stack

# Example usage
stack1 = [1, 2, 3, 4, 5]
output1 = deleteMiddleElement(stack1)
print(output1)  # [1, 2, 4, 5]

stack2 = [1, 2, 3, 4, 5, 6]
output2 = deleteMiddleElement(stack2)
print(output2)  # [1, 2, 4, 5, 6]
