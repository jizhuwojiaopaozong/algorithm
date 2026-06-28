from typing import List

class Solution:
    def islandPerimeter(self, grid:List[List[int]]) -> int:
        res = 0
        x = [0, -1, 0, 1]
        y = [-1, 0, 1, 0]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    for o in range(4):
                        a = i + x[o]
                        b = j + y[o]
                        if a < 0 or a >= len(grid) or b <0  or b >= len(grid[i]):
                            res += 1
                        elif grid[a][b] == 0:
                            res += 1
        return res

solution = Solution()
# print(solution.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
# print(solution.islandPerimeter([[1]]))
print(solution.islandPerimeter([[1, 0]]))