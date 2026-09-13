from typing import List

# 0-1背包求组合问题等价于“在数组中选取一些数，使得这些数的和等于目标值的所有选数组合有多少种”


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if abs(target) > s:
            return 0
        if (target + s) % 2 == 1:
            return 0
        real_target = (target + s) // 2
        f = [0] * (real_target + 1)
        f[0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(real_target, -1, -1):
                if j >= nums[i - 1]:
                    f[j] += f[j - nums[i - 1]]
        return f[real_target]


solution = Solution()
print(solution.findTargetSumWays([1, 1, 1, 1, 1], 3))
print(solution.findTargetSumWays([1], 1))
