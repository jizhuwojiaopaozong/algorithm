class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for c in range(26):
            cur_c = chr(ord('A') + c)
            cnt = 0
            j = 0
            for i in range(len(s)):
                if s[i] == cur_c:
                    cnt += 1
                while i - j + 1 - cnt > k:
                    if s[j] == cur_c:
                        cnt -= 1
                    j += 1
                res = max(res, i - j + 1)
        return res

solution = Solution()
print(solution.characterReplacement("ABAB", 2))