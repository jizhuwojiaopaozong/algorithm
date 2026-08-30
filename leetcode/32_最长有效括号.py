from typing import List


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        res = 0
        start = -1
        for i in range(len(s)):
            if s[i] == "(":
                stk.append(i)
            else:
                if stk:
                    stk.pop(-1)
                    if stk:
                        res = max(res, i - stk[-1])
                    else:
                        res = max(res, i - start)
                else:
                    start = i
        return res

    # 要支持大、中、小三种括号（即 ()、[]、{}），
    def longestValidParentheses2(self, s: str) -> int:
        stk = []
        res = 0
        start = -1
        d = {")": "(", "]": "[", "}": "{"}
        for i in range(len(s)):
            if s[i] in "([{":
                stk.append(i)
            elif s[i] in ")]}":
                if stk and s[stk[-1]] == d[s[i]]:
                    stk.pop(-1)
                    if stk:
                        res = max(res, i - stk[-1])
                    else:
                        res = max(res, i - start)
                else:
                    stk.clear()
                    start = i
        return res

    # follow up 返回最长的有效括号的下标索引，多个的话，返回数组
    def printlongestValidParentheses(self, s: str) -> List[List[int]]:
        stk = []
        res = []
        start = -1
        maxl = 0
        for i in range(len(s)):
            if s[i] == "(":
                stk.append(i)
            else:
                if stk:
                    stk.pop(-1)
                    if stk:
                        curl = i - stk[-1]
                        starti = stk[-1] + 1
                    else:
                        curl = i - start
                        starti = start + 1

                    endi = i
                    if curl > maxl:
                        maxl = curl
                        res = [[starti, endi]]
                    elif curl == maxl:
                        res.append([starti, endi])
                else:
                    start = i
        return res


sol = Solution()
# print(sol.longestValidParentheses("(()"))
# print(sol.printlongestValidParentheses("(()"))
# print(sol.longestValidParentheses(")()())"))
# print(sol.printlongestValidParentheses(")()())"))
# print(sol.longestValidParentheses(""))
# print(sol.printlongestValidParentheses(""))
# print(sol.longestValidParentheses("(()()"))
# print(sol.printlongestValidParentheses("(()()"))
# print(sol.longestValidParentheses("(()())"))
# print(sol.printlongestValidParentheses("(()())"))
# print(sol.longestValidParentheses("(()(()))"))
# print(sol.printlongestValidParentheses("(()(()))"))
# print(sol.longestValidParentheses(""))
# print(sol.printlongestValidParentheses(""))

print(sol.longestValidParentheses2("({[]})"))
# print(sol.printlongestValidParentheses2("({[]})"))
print(sol.longestValidParentheses2("([)]"))
# print(sol.printlongestValidParentheses2("([)]"))
print(sol.longestValidParentheses2("{[()]}()"))
# print(sol.printlongestValidParentheses2("{[()]}()"))
print(sol.longestValidParentheses2("()[{}]"))
# print(sol.printlongestValidParentheses2("()[{}]"))
