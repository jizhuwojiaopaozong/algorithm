class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = [2 ** 31 - 1, 2 ** 31 - 1]
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                while j < k - 1 and nums[i] + nums[j] + nums[k - 1] >= target:
                    k -= 1
                cur = nums[i] + nums[j] + nums[k]
                if abs(cur - target) < res[0]:
                    res[0] = abs(cur - target)
                    res[1] = cur
                if j < k - 1:
                    cur = nums[i] + nums[j] + nums[k - 1]
                    if target - cur < res[0]:
                        res[0] = target -cur
                        res[1] = cur
                j += 1
        return res[1]

solution = Solution()
# print(solution.threeSumClosest([-1, 2, 1, -4], 1))
print(solution.threeSumClosest([0, 0, 0], 1))
