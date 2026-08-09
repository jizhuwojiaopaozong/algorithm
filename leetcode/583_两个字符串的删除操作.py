class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        s1 = " " + s1
        s2 = " " + s2
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            f[i][0] = i
        for j in range(m + 1):
            f[0][j] = j
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                f[i][j] = min(f[i - 1][j] + 1, f[i][j - 1] + 1, f[i - 1][j - 1] + 2)
                if s1[i] == s2[j]:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1])
        return f[n][m]

    def minDistance1(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        s1 = " " + s1
        s2 = " " + s2
        f = [[0] * (m + 1) for i_ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                f[i][j] = max(f[i - 1][j], f[i][j - 1])
                if s1[i] == s2[j]:
                    f[i][j] = max(f[i][j], f[i - 1][j - 1] + 1)
        return n - f[n][m] + m - f[n][m]


solution = Solution()
print(solution.minDistance("sea", "eat"))
print(solution.minDistance1("sea", "eat"))
print(solution.minDistance("leetcode", "etco"))
print(solution.minDistance1("leetcode", "etco"))
