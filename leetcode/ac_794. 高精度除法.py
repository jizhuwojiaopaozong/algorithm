class Solution:
    def cal(self, num1: str, num2: int):
        a = []
        i = 0
        while i < len(num1):
            a.append(int(num1[i]))
            i += 1
        res = []
        t = 0
        for i in range(len(a)):
            t = t * 10 + a[i]
            res.append(t // num2)
            t = t % num2

        while len(res) > 1 and res[0] == 0:
            res.pop(0)

        return res, t


sol = Solution()
num1 = input()
num2 = int(input())
res, t = sol.cal(num1, num2)
print("".join(str(i) for i in res))
print(t)
