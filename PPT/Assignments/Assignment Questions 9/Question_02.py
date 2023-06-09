'''
Given a number n, find the sum of the first natural numbers.

**Example 1:**

Input: n = 3 

Output: 6

**Example 2:**

Input  : 5 

Output : 15
'''
def sum_of_natural_numbers(n):
    return (n * (n + 1)) // 2

print(sum_of_natural_numbers(3))  
print(sum_of_natural_numbers(5))  
