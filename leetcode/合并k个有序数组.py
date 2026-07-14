import heapq
from typing import List


class Solution:
    def mergeKList(self, lists: List[List[int]]) -> List[int]:
        heap = []
        for idx, i in enumerate(lists):
            if i:
                heapq.heappush(heap, (i[0], idx))
        res = []
        while heap:
            tmp, idx = heapq.heappop(heap)
            res.append(tmp)
            lists[idx].pop(0)
            if lists[idx]:
                heapq.heappush(heap, (lists[idx][0], idx))
        return res


solution = Solution()
print(solution.mergeKList([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(solution.mergeKList([[1, 2, 3], [1, 3, 6], [4, 5, 8]]))
