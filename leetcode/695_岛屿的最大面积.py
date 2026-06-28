from typing import List


class Solution:

    def __init__(self):
        self.x = [
            0,
            -1,
            0,
            1,
        ]
        self.y = [-1, 0, 1, 0]

    def dfs(self, grid, i, j):
        tmp = 1
        grid[i][j] = 0
        for o in range(4):
            a = i + self.x[o]
            b = j + self.y[o]
            if (
                a >= 0
                and a <= len(grid) - 1
                and b >= 0
                and b <= len(grid[i]) - 1
                and grid[a][b] == 1
            ):
                tmp += self.dfs(grid, a, b)
        return tmp

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    tmp = self.dfs(grid, i, j)
                    res = max(res, tmp)
        return res


solution = Solution()
# print(solution.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
print(solution.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))
