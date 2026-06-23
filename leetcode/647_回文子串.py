class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            m = i
            n = i
            while m >= 0 and n <= len(s) - 1:
                if s[m] == s[n]:
                    res += 1
                else:
                    break
                m -= 1
                n += 1
            m = i
            n = i + 1
            while m >= 0 and n <= len(s) - 1:
                if s[m] == s[n]:
                    res += 1
                else:
                    break
                m -= 1
                n += 1
        return res

solution = Solution()
# print(solution.countSubstrings("abc"))
print(solution.countSubstrings("aaa"))

