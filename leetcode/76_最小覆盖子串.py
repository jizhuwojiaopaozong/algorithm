from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hs = defaultdict(int)
        ht = defaultdict(int)
        for c in t:
            ht[c] += 1
        i = 0
        j = 0
        res = ""
        cnt = 0
        while i < len(s):
            hs[s[i]] += 1
            if hs[s[i]] <= ht[s[i]]:
                cnt += 1
            while j < len(s) and hs[s[j]] > ht[s[j]]:
                hs[s[j]] -= 1
                j += 1
            if cnt == len(t):
                if not res or i - j + 1 < len(res):
                    res = s[j : i + 1]
            i += 1
        return res


sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))
print(sol.minWindow("a", "a"))
print(sol.minWindow("a", "aa"))
