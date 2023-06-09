'''Given a positive integer, N. Find the factorial of N. 

**Example 1:**

Input: N = 5 

Output: 120

**Example 2:**

Input: N = 4

Output: 24'''

def factorial(N):
    result = 1
    for i in range(1, N+1):
        result *= i
    return result
print(factorial(5))  
print(factorial(4))  
