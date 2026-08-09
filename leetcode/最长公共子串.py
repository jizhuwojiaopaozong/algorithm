class Solution:
    def longestCommonSubstring(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        s1 = " " + s1
        s2 = " " + s2
        f = [[0] * (m + 1) for _ in range(n + 1)]
        res = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i] == s2[j]:
                    f[i][j] = f[i - 1][j - 1] + 1
                    res = max(res, f[i][j])
                else:
                    f[i][j] = 0
        return res

    def printlongestCommonSubstring(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        s1 = " " + s1
        s2 = " " + s2
        f = [[0] * (m + 1) for _ in range(n + 1)]
        res = 0
        end_index = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i] == s2[j]:
                    f[i][j] = f[i - 1][j - 1] + 1
                    if f[i][j] > res:
                        res = f[i][j]
                        end_index = i
                else:
                    f[i][j] = 0
        if res == 0:
            return ""
        else:
            return s1[end_index - res + 1 : end_index + 1]


solution = Solution()
print(solution.longestCommonSubstring("ABCD", "ABDC"))
print(solution.printlongestCommonSubstring("ABCD", "ABDC"))
print(solution.longestCommonSubstring("a", ""))
print(solution.printlongestCommonSubstring("a", ""))
print(solution.longestCommonSubstring("a", "a"))
print(solution.printlongestCommonSubstring("a", "a"))
