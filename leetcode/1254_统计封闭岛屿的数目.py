from typing import List


class Solution:
    def __init__(self):
        self.x = [0, -1, 0, 1]
        self.y = [-1, 0, 1, 0]

    def dfs(self, grid, i, j):
        tmp = 1
        grid[i][j] = 1
        for o in range(4):
            a = i + self.x[o]
            b = j + self.y[o]
            if a < 0 or a >= len(grid) or b < 0 or b >= len(grid[i]):
                tmp = 0
            elif grid[a][b] == 0 and not self.dfs(grid, a, b):
                tmp = 0
        return tmp

    def closedIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    res += self.dfs(grid, i, j)
        return res

solution = Solution()
# print(solution.closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))
# print(solution.closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]))
print(solution.closedIsland([[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]))