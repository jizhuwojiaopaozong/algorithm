from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1

    # 输出所有的重复元素
    def findRepeatNumber1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set()
        for i in range(n):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    s.add(nums[i])
                    break
                else:
                    index = nums[i]
                    nums[index], nums[i] = nums[i], nums[index]
        return list(s)


s = Solution()

# print(s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
print(s.findRepeatNumber1([2, 3, 1, 0, 2, 5, 3]))
print(s.findRepeatNumber1([2, 3, 1, 2, 2, 5, 3]))
