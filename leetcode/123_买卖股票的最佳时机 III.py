from typing import List


class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        f = [0] * (len(nums) + 1)
        minp = float("inf")
        for i in range(1, len(nums) + 1):
            f[i] = max(f[i - 1], nums[i - 1] - minp)
            minp = min(minp, nums[i - 1])

        res = 0
        maxp = float("-inf")
        i = len(nums)
        while i:
            res = max(res, f[i - 1] + maxp - nums[i - 1])
            maxp = max(maxp, nums[i - 1])
            i -= 1
        return res

solution = Solution()
print(solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
print(solution.maxProfit([1, 2, 3, 4, 5]))
print(solution.maxProfit([7, 6, 4, 3, 1]))
print(solution.maxProfit([1, 2, 3, 4, 5]))
print(solution.maxProfit([1, 2, 3, 4, 5]))
