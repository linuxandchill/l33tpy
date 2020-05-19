from typing import List 

def findJudge(N: int, trust: List[List[int]]) -> int:
    holder = [0]*(N+1)

    for x, y in trust:
        print(holder[x],holder[y])
        holder[x] -= 1
        holder[y] += 1
        print(holder[x],holder[y])

    for i, value in enumerate(holder):
        if value == N - 1:
            return i

    return -1 


print(findJudge(2, [[1,2]]))
