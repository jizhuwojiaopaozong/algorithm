class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            m = i - 1
            n = i + 1
            while m >= 0 and n <= len(s) - 1 and s[m] == s[n]:
                m -= 1
                n += 1
            if n - m - 1 > len(res):
                res = s[m + 1 : n]
            m = i
            n = i + 1
            while m >= 0 and n <= len(s) - 1 and s[m] == s[n]:
                m -= 1
                n += 1
            if n - m - 1 > len(res):
                res = s[m + 1 : n]
        return res


solution = Solution()
print(solution.longestPalindrome("babad"))