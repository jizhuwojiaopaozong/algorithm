from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stk = []
        res = []
        for i in range(len(nums)):
            if stk and i - k + 1 > stk[0]:
                stk.pop(0)
            while stk and nums[stk[-1]] <= nums[i]:
                stk.pop(-1)
            stk.append(i)
            if i - k + 1 >= 0:
                res.append(nums[stk[0]])
        return res


sol = Solution()
print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(sol.maxSlidingWindow([1], 1))
