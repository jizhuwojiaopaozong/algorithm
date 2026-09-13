class Solution:
    def reverseWords(self, s: str) -> str:
        sl = list(s)
        i = 0
        k = 0
        while i < len(sl):
            if sl[i] == " ":
                i += 1
                continue
            j = i
            t = k
            while j < len(sl) and sl[j] != " ":
                sl[t] = sl[j]
                j += 1
                t += 1
            sl[k:t] = sl[k:t][::-1]
            if t != len(sl):
                sl[t] = " "
                t += 1
            k = t
            i = j
        if k and sl[k - 1] == " ":
            k -= 1
        return "".join(sl[:k][::-1])

    def reverseWords2(self, s: str) -> str:
        # return " ".join([word[::-1] for word in s.split()])[::-1]
        # 下述写法错误：因为 Python 中的 .reverse() 方法返回的是 None，而不是反转后的列表。.reverse()：对这个列表进行原地反转
        # return " ".join(s.split().reverse())
        # reversed() 不是列表的方法，而是 Python 的内置函数。它不会修改原列表，而是返回一个反转的迭代器，可以直接被 join 消费。
        return " ".join(reversed(s.split()))

    def reverseWords3(self, s: str) -> str:
        return ".".join(s.split(".")[::-1])


sol = Solution()
# print(sol.reverseWords("the sky is blue"))
# print(sol.reverseWords("  hello world  "))
# print(sol.reverseWords("a good   example"))
print(sol.reverseWords3("www.kuaishou.com"))
