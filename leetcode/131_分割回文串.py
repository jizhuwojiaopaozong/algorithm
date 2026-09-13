from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    f[i][j] = True
                elif s[i] == s[j]:
                    if i + 1 > j - 1 or f[i + 1][j - 1]:
                        f[i][j] = True
        res = []
        path = []

        def dfs(index):
            if index == n:
                res.append(path[:])
                return
            else:
                for i in range(index, n):
                    if f[index][i]:
                        path.append(s[index : i + 1])
                        dfs(i + 1)
                        path.pop()

        dfs(0)
        return res


sol = Solution()
print(sol.partition("aab"))
print(sol.partition("a"))
print(sol.partition("ab"))
