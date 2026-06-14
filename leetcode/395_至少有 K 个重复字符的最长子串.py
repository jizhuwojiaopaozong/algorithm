from collections import defaultdict

class Solution:
    def add(self, c, k):
        if self.d[c] == 0:
            self.x += 1
        self.d[c] += 1
        if self.d[c] == k:
            self.y += 1
    
    def delete(self, c, k):
        if self.d[c] == k:
            self.y -= 1
        self.d[c] -= 1
        if self.d[c] == 0:
            self.x -= 1

    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for m in range(1, 27):
            self.d = defaultdict(int)
            self.x = 0
            self.y = 0
            j = 0
            for i in range(len(s)):
                self.add(s[i], k)
                while self.x > m:
                    self.delete(s[j], k)
                    j += 1
                if self.x == self.y:
                    res = max(res, i - j + 1)
        return res

solution = Solution()
print(solution.longestSubstring("ababbc", 2))