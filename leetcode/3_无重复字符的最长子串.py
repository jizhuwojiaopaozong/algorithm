from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sum = 0
        d = defaultdict(int)
        j = 0
        for i in range(len(s)):
            d[s[i]] += 1
            while d[s[i]] > 1:
                d[s[j]] -= 1
                j += 1
            sum = max(sum, i - j +1)
        return sum