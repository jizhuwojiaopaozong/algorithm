class Solution:
    def isOneEditDistance(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if m > n:
            return self.isOneEditDistance(s2, s1)
        if n - m > 1:
            return False
        for i in range(m):
            if s1[i] != s2[i]:
                if n == m:
                    return s1[i + 1 :] == s2[i + 1 :]
                else:
                    return s1[i + 1 :] == s2[i:]
        return n != m


solution = Solution()
print(solution.isOneEditDistance("ab", "acb"))
print(solution.isOneEditDistance("cab", "ad"))
print(solution.isOneEditDistance("1203", "1213"))
print(solution.isOneEditDistance("a", ""))
print(solution.isOneEditDistance("", ""))
