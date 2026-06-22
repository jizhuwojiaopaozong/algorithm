class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                m = j + 1
                n = len(nums) - 1
                while m < n:
                    if m > j + 1 and nums[m] == nums[m - 1]:
                        m += 1
                        continue
                    while (
                        m < n - 1
                        and nums[i] + nums[j] + nums[m] + nums[n - 1] >= target
                    ):
                        n -= 1
                    if nums[i] + nums[j] + nums[m] + nums[n] == target:
                        res.append([nums[i], nums[j], nums[m], nums[n]])
                    m += 1
        return res

solution = Solution()
# print(solution.fourSum([1, 0, -1, 0, -2, 2], 0))
print(solution.fourSum([2, 2, 2, 2, 2], 8))
