class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        word1 = " " + word1
        word2 = " " + word2
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            f[i][0] = i
        for i in range(m + 1):
            f[0][i] = i
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                f[i][j] = min(f[i - 1][j], f[i][j - 1]) + 1
                if word1[i] == word2[j]:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1])
                else:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1] + 1)
        return f[n][m]
