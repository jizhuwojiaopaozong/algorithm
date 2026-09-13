from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        f = [[float("inf")] * (target + 1) for _ in range(len(nums) + 1)]
        f[0][0] = 0
        for i in range(1, len(nums) + 1):
            for j in range(0, target + 1):
                f[i][j] = f[i - 1][j]
                if j >= nums[i - 1]:
                    f[i][j] = min(f[i][j], f[i - 1][j - nums[i - 1]] + 1)
        if f[len(nums)][target] == float("inf"):
            return False
        else:
            return True


solution = Solution()
print(solution.canPartition([1, 5, 11, 5]))
print(solution.canPartition([1, 2, 3, 5]))
