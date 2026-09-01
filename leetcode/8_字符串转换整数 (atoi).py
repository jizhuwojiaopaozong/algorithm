class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i == len(s):
            return 0
        flag = 1
        if s[i] == "-":
            flag = -1
            i += 1
        elif s[i] == "+":
            i += 1
        res = 0
        while i < len(s) and s[i] >= "0" and s[i] <= "9":
            res = res * 10 + int(s[i])
            i += 1
        res = res * flag
        if res > INT_MAX:
            return INT_MAX
        elif res < INT_MIN:
            return INT_MIN
        else:
            return res


sol = Solution()
print(sol.myAtoi("42"))
print(sol.myAtoi("   -042"))
print(sol.myAtoi("4193 with words"))
print(sol.myAtoi("0-1"))
print(sol.myAtoi("words and 987"))
print(sol.myAtoi("-91283472332"))
print(sol.myAtoi("3.14159"))
print(sol.myAtoi("+-12"))
print(sol.myAtoi("   +0 123"))
print(sol.myAtoi("2147483648"))
print(sol.myAtoi("-2147483649"))
