from collections import defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        n = len(s)
        word_len = len(words[0])
        word_num = len(words)
        total_len = word_len * word_num
        if total_len > n:
            return []
        word_h = defaultdict(int)
        for c in words:
            word_h[c] += 1
        res = []
        for i in range(word_len):
            cur_h = defaultdict(int)
            left = i
            valid_num = 0
            for j in range(i, n - word_len + 1, word_len):
                tmp = s[j : j + word_len]
                if tmp in word_h:
                    cur_h[tmp] += 1
                    valid_num += 1

                    while cur_h[tmp] > word_h[tmp]:
                        cur_h[s[left : left + word_len]] -= 1
                        left += word_len
                        valid_num -= 1

                    if valid_num == word_num:
                        res.append(left)
                else:
                    cur_h.clear()
                    valid_num = 0
                    left = j + word_len
        return res


sol = Solution()
print(sol.findSubstring("barfoothefoobarman", ["foo", "bar"]))
print(sol.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
print(sol.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))