class Solution:
    def checkValidString(self, s: str) -> bool:
        # low 代表“最少需要几个左括号”，不够的话可以用 * 当空字符串凑，所以 low 最小是 0。
        # high 代表“最多能有几个左括号”，如果 high < 0（即 low > high），说明 * 全变成 ( 都不够，直接 return False。
        low = 0
        high = 0
        for c in s:
            if c == "(":
                low += 1
                high += 1
            elif c == ")":
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1
            low = max(low, 0)
            if low > high:
                return False
        return not low


solution = Solution()
print(solution.checkValidString("()"))
print(solution.checkValidString("(*)"))
print(solution.checkValidString("(*))"))
print(solution.checkValidString("((*)"))
print(solution.checkValidString("((*))"))
print(solution.checkValidString("((*)*)"))
print(solution.checkValidString("((*)*))"))
print(solution.checkValidString("((*)*)*"))
print(solution.checkValidString("((*)*)*))"))
