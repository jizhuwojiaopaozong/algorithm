class Solution:
    def reverseWords(self, s: str) -> str:
        sl = list(s)
        i = 0
        while i < len(sl):
            if sl[i] == " ":
                i += 1
                continue
            j = i
            while j < len(s) and sl[j] != " ":
                j += 1
            sl[i:j] = sl[i:j][::-1]
            i = j
        return "".join(sl)


sol = Solution()
print(sol.reverseWords("    Let's take LeetCode    contest"))
print(sol.reverseWords("Mr Ding"))
