from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stk = []
        last = 0
        for i in range(len(height)):
            while stk and height[stk[-1]] <= height[i]:
                res += (i - stk[-1] - 1) * (height[stk[-1]] - last)
                last = height[stk[-1]]
                stk.pop(-1)
            if stk:
                res += (i - stk[-1] - 1) * (height[i] - last)
            stk.append(i)
        return res


solution = Solution()
print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(solution.trap([4, 2, 0, 3, 2, 5]))
