class Solution:
    def cal(self, num1: str, num2: int):
        a = []
        i = len(num1) - 1
        while i >= 0:
            a.append(int(num1[i]))
            i -= 1
        res = []
        t = 0
        i = 0
        while i < len(a) or t:
            if i < len(a):
                t += a[i] * num2
            res.append(t % 10)
            t = t // 10
            i += 1

        while len(res) > 1 and res[-1] == 0:
            res.pop(-1)

        return res


sol = Solution()
num1 = input()
num2 = int(input())
res = sol.cal(num1, num2)
print("".join(str(i) for i in res[::-1]))
