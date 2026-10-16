class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        f = [[0] * n for o in range(n)]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = length + i - 1
                if i == j:
                    f[i][j] = 1
                else:
                    if s[i] == s[j]:
                        f[i][j] = f[i + 1][j - 1] + 2
                    f[i][j] = max(f[i][j], max(f[i][j - 1], f[i + 1][j]))
        return f[0][n - 1]

    def longestPalindromeSubseq_print(self, s: str) -> str:
        n = len(s)
        f = [[0] * n for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                j = l + i - 1
                if i == j:
                    f[i][j] = 1
                else:
                    if s[i] == s[j]:
                        f[i][j] = f[i + 1][j - 1] + 2
                    f[i][j] = max(f[i][j], max(f[i + 1][j], f[i][j - 1]))

        i = 0
        j = n - 1
        left = []
        right = []
        while i < j:
            if s[i] == s[j]:
                left.append(s[i])
                right.append(s[j])
                i += 1
                j -= 1
            elif f[i + 1][j] > f[i][j - 1]:
                i += 1
            else:
                j -= 1
        mid = s[i] if i == j else ""
        return "".join(left) + mid + "".join(reversed(right))


sol = Solution()
print(sol.longestPalindromeSubseq_print("bbbab"))
print(sol.longestPalindromeSubseq_print("abcda"))
print(sol.longestPalindromeSubseq_print("abcd"))
