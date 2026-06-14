from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        d = defaultdict(int)
        j = 0
        for i in range(len(s)):
            d[s[i]] += 1
            while d[s[i]] > 2:
                d[s[j]] -= 1
                j +=1
            res = max(res, i-j+1)
        return res

solution = Solution()
# 5
# print(solution.lengthOfLongestSubstring("abaccc"))
# 6
print(solution.lengthOfLongestSubstring("abcabcbb"))
