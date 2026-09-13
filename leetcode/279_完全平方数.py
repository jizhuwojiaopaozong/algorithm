class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i**2 for i in range(1, 101)]
        f = [[float("inf")] * (n + 1) for _ in range(len(nums) + 1)]
        f[0][0] = 0
        for i in range(1, len(nums) + 1):
            for j in range(0, n + 1):
                f[i][j] = f[i - 1][j]
                if j >= nums[i - 1]:
                    f[i][j] = min(f[i][j], f[i][j - nums[i - 1]] + 1)
        return f[len(nums)][n]


solution = Solution()
print(solution.numSquares(12))
print(solution.numSquares(13))
