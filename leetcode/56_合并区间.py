from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if not intervals:
            return res
        intervals.sort()
        l = intervals[0][0]
        r = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > r:
                res.append([l, r])
                l = intervals[i][0]
                r = intervals[i][1]
            else:
                r = max(r, intervals[i][1])
        res.append([l, r])
        return res

solution = Solution()
print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))
print(solution.merge([[1,4],[4,5]]))
print(solution.merge([[4,7],[1,4]]))
