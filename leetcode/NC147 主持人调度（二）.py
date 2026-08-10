from typing import List
import heapq


class Solution:
    def minmumNumberOfHost(self, n: int, arr: List[List[int]]) -> int:
        heap = []
        arr.sort(key=lambda x: x[0])
        for i in range(n):
            if not heap or heap[0] > arr[i][0]:
                heapq.heappush(heap, arr[i][1])
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, arr[i][1])
        return len(heap)
