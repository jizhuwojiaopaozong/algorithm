from typing import List


class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        res = 0
        minf = float("inf")
        for i in range(len(nums)):
            res = max(res, nums[i] - minf)
            minf = min(minf, nums[i])
        return res

solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit([7, 6, 4, 3, 1]))