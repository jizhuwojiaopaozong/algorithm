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


solution = Solution()
print(solution.numDistinct("rabbbit", "rabbit"))
print(solution.numDistinct("babgbag", "bag"))