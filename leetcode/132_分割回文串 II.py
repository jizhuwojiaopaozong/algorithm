class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        s = " " + s
        f = [[False] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1, 0, -1):
            for j in range(i, n + 1):
                if i == j:
                    f[i][j] = True
                elif s[i] == s[j]:
                    if i + 1 > j - 1 or f[i + 1][j - 1]:
                        f[i][j] = True

        g = [float("inf")] * (n + 1)
        g[0] = 0
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if f[j][i]:
                    g[i] = min(g[i], g[j - 1] + 1)
        return g[n] - 1


s = Solution()
print(s.minCut("aab"))
print(s.minCut("a"))
print(s.minCut("ab"))
