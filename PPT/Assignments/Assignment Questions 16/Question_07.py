'''Given a sequence of n strings, the task is to check if any two similar words come together and then destroy each other then print the number of words left in the sequence after this pairwise destruction.

**Examples:**

Input : ab aa aa bcd ab

Output : 3

*As aa, aa destroys each other so,*

*ab bcd ab is the new sequence.*

Input :  tom jerry jerry tom

Output : 0

*As first both jerry will destroy each other.*

*Then sequence will be tom, tom they will also destroy*

*each other. So, the final sequence doesn’t contain any*

*word.*'''

def countWordsAfterDestruction(words):
    stack = []
    
    for word in words:
        if not stack or word != stack[-1]:
            stack.append(word)
        else:
            stack.pop()
    
    return len(stack)

# Example usage
sequence = ['ab', 'aa', 'aa', 'bcd', 'ab']
result = countWordsAfterDestruction(sequence)
print(result)  # Output: 3

sequence = ['tom', 'jerry', 'jerry', 'tom']
result = countWordsAfterDestruction(sequence)
print(result)  # Output: 0
