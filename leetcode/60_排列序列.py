class Solution:
    def getPermutation(self, n, k):
        res = ""
        state = [False] * n
        for i in range(1, n + 1):
            fact = 1
            for j in range(1, n - i + 1):
                fact *= j
            for p in range(1, n + 1):
                if not state[p - 1]:
                    if k > fact:
                        k -= fact
                    else:
                        res += str(p)
                        state[p - 1] = True
                        break
        return res

solution = Solution()
print(solution.getPermutation(3, 3))
print(solution.getPermutation(4, 9))
print(solution.getPermutation(3, 1))
print(solution.getPermutation(3, 2))
print(solution.getPermutation(3, 3))
print(solution.getPermutation(3, 4))
print(solution.getPermutation(3, 5))
print(solution.getPermutation(3, 6))
print(solution.getPermutation(3, 7))
print(solution.getPermutation(3, 8))
print(solution.getPermutation(3, 9))