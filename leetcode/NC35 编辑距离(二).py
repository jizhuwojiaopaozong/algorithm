class Solution:
    def minEditCost(self, str1: str, str2: str, ic: int, dc: int, rc: int) -> int:
        n = len(str1)
        m = len(str2)
        str1 = " " + str1
        str2 = " " + str2
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            f[i][0] = i * dc
        for i in range(m + 1):
            f[0][i] = i * ic
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                f[i][j] = min(f[i - 1][j] + dc, f[i][j - 1] + ic)
                if str1[i] == str2[j]:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1])
                else:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1] + rc)
        return f[n][m]


sol = Solution()
print(sol.minEditCost("abc", "adc", 5, 3, 2))
print(sol.minEditCost("abc", "adc", 5, 3, 100))
