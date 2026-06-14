from collections import defaultdict

class Solution:
    """
    @param s: a string
    @return: the length of the longest substring T that contains at most 2 distinct characters
    """
    def add(self, c):
        if self.d[c] == 0:
            self.cnt += 1
        self.d[c] += 1
    
    def delete(self, c):
        if self.d[c] == 1:
            self.cnt -= 1
        self.d[c] -= 1

    def length_of_longest_substring_two_distinct(self, s: str) -> int:
        # Write your code here
        res = 0
        self.d = defaultdict(int)
        self.cnt = 0
        j = 0
        for i in range(len(s)):
            self.add(s[i])
            while self.cnt > 2:
                self.delete(s[j])
                j += 1
            res = max(res, i - j + 1)
        return res