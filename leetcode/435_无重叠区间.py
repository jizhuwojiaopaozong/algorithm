class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        res = 1
        r = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= r:
                res += 1
                r = intervals[i][1]
        return len(intervals) - res


sol = Solution()
print(sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
print(sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))  # [1,2], [2,3], [3,4]
print(sol.eraseOverlapIntervals([[1, 2], [2, 3]]))  # [1,2], [2,3], [3,4]
