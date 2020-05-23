from typing import List
# from queue import PriorityQueue
import heapq

def main(nums: List[int], k: int ) -> int:
    q = []

    for n in nums:
        if len(q) < k:
            heapq.heappush(q, n)
            print("Adding")
            print(q)
        else:
            heapq.heappushpop(q, n)
            print(q)
            print("Removing")

    return q[0]
 
main([3,2,1,5,6,4], 3)

