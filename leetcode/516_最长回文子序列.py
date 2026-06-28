class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        f = [[0] * n for o in range(n)]
        for length in range(1, n+1):
            for i in range(n - length + 1):
                j = length + i - 1
                if i == j:
                    f[i][j] = 1
                else:
                    if s[i] == s[j]:
                        f[i][j] = f[i+1][j-1] + 2
                    f[i][j] = max(f[i][j], max(f[i][j-1], f[i+1][j]))
        return f[0][n-1]