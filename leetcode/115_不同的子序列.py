class Solution:
    def numDistinct(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        s1 = " " + s1
        s2 = " " + s2
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            f[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                f[i][j] = f[i - 1][j]
                if s1[i] == s2[j]:
                    f[i][j] += f[i - 1][j - 1]
        return f[n][m]

    def numDistinct_print(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        s1 = " " + s1
        s2 = " " + s2
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            f[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                f[i][j] = f[i - 1][j]
                if s1[i] == s2[j]:
                    f[i][j] += f[i - 1][j - 1]
        res = []
        path = []

        def dfs(i, j):
            if j == 0:
                res.append(path[::-1])
                return
            if f[i - 1][j] > 0:
                dfs(i - 1, j)
            if s1[i] == s2[j] and f[i - 1][j - 1] > 0:
                path.append(i - 1)
                dfs(i - 1, j - 1)
                path.pop()

        dfs(n, m)
        return res


solution = Solution()
print(solution.numDistinct("rabbbit", "rabbit"))
print(solution.numDistinct("babgbag", "bag"))
print(solution.numDistinct_print("rabbbit", "rabbit"))
print(solution.numDistinct_print("babgbag", "bag"))
