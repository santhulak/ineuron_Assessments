'''iven a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
**Input:** n = 3

**Output:** [[1,2,3],[8,9,4],[7,6,5]]'''

def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]  # Initialize the matrix with zeros
    num = 1  # Starting element value
    top, bottom, left, right = 0, n - 1, 0, n - 1  # Initialize boundaries

    while num <= n * n:
        # Traverse from left to right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Traverse from right to left
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # Traverse from bottom to top
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix


n = 3
result = generateMatrix(n)
print(result)
