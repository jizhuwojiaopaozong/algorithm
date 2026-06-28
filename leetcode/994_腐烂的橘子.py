from typing import List
from queue import Queue


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = Queue()
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.put([i, j])

        if q.empty():
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1:
                        return -1
            return 0

        x = [0, -1, 0, 1]
        y = [-1, 0, 1, 0]

        res = -1
        while not q.empty():
            res += 1
            cur_b = q.qsize()
            while cur_b:
                cur_b -= 1
                i, j = q.get()
                for o in range(4):
                    a = i + x[o]
                    b = j + y[o]
                    if a < 0 or a >= n or b < 0 or b >= m or grid[a][b] != 1:
                        continue
                    else:
                        grid[a][b] = 2
                        q.put([a, b])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return res


solution = Solution()
# print(solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
# print(solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(solution.orangesRotting([[0,2]]))