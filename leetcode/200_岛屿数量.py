from typing import List


class Solution:

    def __init__(self):
        self.x = [0, -1, 0, 1]
        self.y = [-1, 0, 1, 0]

    def dfs(self, grid, i, j):
        grid[i][j] = "0"
        for o in range(4):
            a = i + self.x[o]
            b = j + self.y[o]
            if (
                a >= 0
                and a <= len(grid) - 1
                and b >= 0
                and b <= len(grid[i]) - 1
                and grid[a][b] == "1"
            ):
                self.dfs(grid, a, b)

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    res += 1
        return res


solution = Solution()
# print(solution.numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
print(solution.numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))