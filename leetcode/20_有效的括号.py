class Solution:
    def isValid(self, s: str) -> bool:
        map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c not in map:
                stack.append(c)
            else:
                if not stack or stack.pop() != map[c]:
                    return False
        return not stack


    # 不要求一一闭合，则就不需要栈。只要左右括号数量相同即可。
    def isValid(self, s:str)-> bool:
        l1 = 0
        l2 = 0
        l3 = 0
        for c in s:
            if c == '(':
                l1 += 1
            elif c == ')':
                l1 -= 1
            elif c == '[':
                l2 += 1
            elif c == ']':
                l2 -= 1
            elif c == '{':
                l3 += 1
            else:
                l3 -= 1
            if l1 < 0 or l2 < 0 or l3 < 0:
                return False
        return l1 == 0 and l2 ==0 and l3 ==0

solution = Solution()
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("([)]"))
print(solution.isValid("{[]}"))
print(solution.isValid("["))
print(solution.isValid("]"))
print(solution.isValid("("))
print(solution.isValid(")"))