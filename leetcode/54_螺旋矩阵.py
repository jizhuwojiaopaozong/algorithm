from typing import List


class Solution:
    def spiralOrder(selfself, matrix: List[List[int]]) -> List[int]:
        res = []
        n = len(matrix)
        if not n:
            return res
        m = len(matrix[0])
        state = [[False] * m for _ in range(n)]
        x = 0
        y = 0
        d = 0
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(n * m):
            res.append(matrix[x][y])
            state[x][y] = True
            if i == n * m - 1:
                break
            a = x + dx[d]
            b = y + dy[d]
            while a < 0 or a >= n or b < 0 or b >= m or state[a][b]:
                d = (d + 1) % 4
                a = x + dx[d]
                b = y + dy[d]
            x = a
            y = b
        return res


sol = Solution()
print(sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(sol.spiralOrder([[1], [2]]))
