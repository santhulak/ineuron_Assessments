'''
💡 You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.

Given the integer n, return *the number of **complete rows** of the staircase you will build*.

**Example 1:**

[]()

![v2.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4bd91cfa-d2b1-47b3-8197-a72e8dcfff4b/v2.jpg)

**Input:** n = 5

**Output:** 2

**Explanation:** Because the 3rd row is incomplete, we return 2.

'''

def arrangeCoins(n):
    left = 0
    right = n

    while left <= right:
        k = left + (right - left) // 2
        curr = k * (k + 1) // 2

        if curr == n:
            return k

        if curr > n:
            right = k - 1
        else:
            left = k + 1

    return right

# Test the function
n = 5
result = arrangeCoins(n)
print(result)
