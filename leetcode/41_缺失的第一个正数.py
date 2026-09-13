from typing import List


# 原地哈希
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 1
        for i in range(n):
            if nums[i] != -(2**31):
                nums[i] -= 1
        for i in range(n):
            while (
                nums[i] >= 0
                and nums[i] < n
                and i != nums[i]
                and nums[nums[i]] != nums[i]
            ):
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            # 下面是死循环写法
            #  nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
        for i in range(n):
            if i != nums[i]:
                return i + 1
        return n + 1

    # 变形题，缺失的第一个比K大的数字
    def firstMissingGreaterThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return k + 1
        for i in range(n):
            if nums[i] > k:
                nums[i] -= k + 1
            else:
                nums[i] = -(2**31)
        for i in range(n):
            while (
                nums[i] >= 0
                and nums[i] < n
                and i != nums[i]
                and nums[nums[i]] != nums[i]
            ):
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        for i in range(n):
            if i != nums[i]:
                return i + k + 1
        return n + k + 1


s = Solution()
# print(s.firstMissingPositive([1, 2, 0]))
# print(s.firstMissingPositive([3, 4, -1, 1]))
# print(s.firstMissingPositive([7, 8, 9, 11, 12]))
print(s.firstMissingGreaterThanK([1, 2, 0], 0))  # 3
print(s.firstMissingGreaterThanK([3, 4, -1, 1], 2))  # 5
print(s.firstMissingGreaterThanK([7, 8, 9, 11, 12], 5))  # 6
