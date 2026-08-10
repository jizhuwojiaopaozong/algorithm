class Solution:
    # 输出最长公共子序列的长度
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        s1 = " " + s1
        s2 = " " + s2
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                f[i][j] = max(f[i - 1][j], f[i][j - 1])
                if s1[i] == s2[j]:
                    f[i][j] = max(f[i][j], f[i - 1][j - 1] + 1)
        return f[n][m]

    # 输出最长公共子序列

    def printlongestCommonSubsequence(self, s1: str, s2: str) -> str:
        n = len(s1)
        m = len(s2)
        s1 = " " + s1
        s2 = " " + s2
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                f[i][j] = max(f[i - 1][j], f[i][j - 1])
                if s1[i] == s2[j]:
                    f[i][j] = max(f[i][j], f[i - 1][j - 1] + 1)
        res = []
        i = n
        j = m
        while i >= 1 and j >= 1:
            if s1[i] == s2[j]:
                res.append(s1[i])
                i -= 1
                j -= 1
            elif f[i - 1][j] > f[i][j - 1]:
                i -= 1
            else:
                j -= 1
        return "".join(res[::-1])


sol = Solution()

print(sol.longestCommonSubsequence("abcde", "ace"))
print(sol.printlongestCommonSubsequence("abcde", "ace"))
print(sol.longestCommonSubsequence("abc", "abc"))
print(sol.printlongestCommonSubsequence("abc", "abc"))
print(sol.longestCommonSubsequence("abc", "def"))
print(sol.printlongestCommonSubsequence("abc", "def"))
