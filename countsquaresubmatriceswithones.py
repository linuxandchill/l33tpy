from typing import List

def countSquares(matrix: List[List[int]]) -> int:
    holder = []
    total = 0

    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            if (matrix[row][col]) == 1:
                holder.append(1)
          

    print(len(holder))
countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
])

