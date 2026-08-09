class Solution:
    def multiply(self, num1: str, num2: str) -> str:
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
        c = [0] * (len(a) + len(b))
        for i in range(len(a)):
            for j in range(len(b)):
                c[i + j] += a[i] * b[j]
        t = 0
        for i in range(len(c)):
            t += c[i]
            c[i] = t % 10
            t = t // 10
        k = len(c) - 1
        while k > 0 and c[k] == 0:
            k -= 1
        res = ""
        while k >= 0:
            res += str(c[k])
            k -= 1
        return res

solution = Solution()
print(solution.multiply("2", "3"))
print(solution.multiply("123", "456"))