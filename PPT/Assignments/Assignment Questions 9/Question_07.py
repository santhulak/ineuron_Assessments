'''Given a string S, the task is to write a program to print all permutations of a given string.

**Example 1:**

***Input:***

*S = “ABC”*

***Output:***

*“ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”*

**Example 2:**

***Input:***

*S = “XY”*

***Output:***

*“XY”, “YX”*'''

def permute(s):
    # Convert the string to a list of characters
    chars = list(s)
    # Store the permutations
    permutations = []
    # Generate permutations using backtracking
    backtrack(chars, 0, len(s) - 1, permutations)
    # Return the permutations as a list of strings
    return [''.join(p) for p in permutations]

def backtrack(chars, start, end, permutations):
    if start == end:
        # Base case: reached the end of the string, add the permutation to the list
        permutations.append(chars[:])
    else:
        # Generate permutations by swapping characters
        for i in range(start, end + 1):
            # Swap characters
            chars[start], chars[i] = chars[i], chars[start]
            # Recursively generate permutations
            backtrack(chars, start + 1, end, permutations)
            # Undo the swap
            chars[start], chars[i] = chars[i], chars[start]

# Test the function with examples
s1 = "ABC"
print(permute(s1))  

s2 = "XY"
print(permute(s2))  
