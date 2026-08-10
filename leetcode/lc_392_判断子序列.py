class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = 0
        for c in t:
            if k < len(s) and s[k] == c:
                k += 1
        return k == len(s)
