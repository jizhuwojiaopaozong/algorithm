from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        if not points:
            return 0
        res = 1
        r = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > r:
                res += 1
                r = points[i][1]
        return res
