class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        a = []
        b = []
        i = len(num1) - 1
        while i >= 0:
            a.append(int(num1[i]))
            i -= 1
        i = len(num2) - 1
        while i >= 0:
            b.append(int(num2[i]))
            i -= 1
        res = []
        i = 0
        j = 0
        c = 0
        while i < len(a) or j < len(b) or c:
            if i < len(a):
                c += a[i]
            if j < len(b):
                c += b[j]
            res.append(c % 10)
            c = c // 10
            i += 1
            j += 1
        return "".join(str(i) for i in res[::-1])


solution = Solution()
print(solution.addStrings("11", "123"))
print(solution.addStrings("456", "77"))
print(solution.addStrings("0", "0"))
