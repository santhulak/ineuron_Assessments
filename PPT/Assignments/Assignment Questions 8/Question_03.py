'''Given two strings word1 and word2, return *the minimum number of **steps** required to make* word1 *and* word2 *the same*.

In one **step**, you can delete exactly one character in either string.

**Example 1:**

**Input:** word1 = "sea", word2 = "eat"

**Output:** 2

**Explanation:** You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

'''
def minDistance(word1, word2):
    m = len(word1)
    n = len(word2)

    # Initialize the dp array
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill in the dp array
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[m][n]

# Test the function
word1 = "sea"
word2 = "eat"
result = minDistance(word1, word2)
print(result)
