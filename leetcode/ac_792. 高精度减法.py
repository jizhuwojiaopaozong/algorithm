class Solution:
    def cal(self, num1, num2):
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
        t = 0
        for i in range(len(a)):
            t = a[i] - t
            if i < len(b):
                t = t - b[i]
            res.append((t + 10) % 10)
            if t < 0:
                t = 1
            else:
                t = 0
        while len(res) > 1 and res[-1] == 0:
            res.pop(-1)
        return res

    def cmp(self, num1, num2):
        if len(num1) != len(num2):
            return len(num1) > len(num2)
        else:
            for i in range(len(num1)):
                if num1[i] != num2[i]:
                    return int(num1[i]) > int(num2[i])
            return True


sol = Solution()
num1 = input()
num2 = input()
if sol.cmp(num1, num2):
    res = sol.cal(num1, num2)
    print("".join(str(i) for i in res[::-1]))
else:
    res = sol.cal(num2, num1)
    print("-" + "".join(str(i) for i in res[::-1]))
