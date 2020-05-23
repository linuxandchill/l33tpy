from typing import List

def maximalSquare(matrix: List[List[str]]) -> int:
    m = len(matrix)
    n = len(matrix[0])
    if m == 0:
        return 0

    height = 0
    print(matrix)
    final = [[0]* (n+1) for _ in range(m+1)]
    print(final)

    for i in range(0,m):
        for j in range(0, n):
            if matrix[i-1][j-1] == '1':
                final[i][j] = 1 + min(final[i-1][j], final[i][j-1], final[i-1][j-1])

                height = max(height, final[i][j])

    return height**2


arr = [[1, 0, 1, 0, 0],[1 ,0 ,1 ,1, 1],[1, 1 ,1 ,1 ,1],[1, 0, 0, 1, 0]]
print(maximalSquare(arr))


