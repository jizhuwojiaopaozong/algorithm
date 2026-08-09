from typing import List


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: List[int]) -> List[int]:
        stk = []
        q = [-1] * len(nums2)
        i = len(nums2) - 1
        while i >= 0:
            x = nums2[i]
            while stk and stk[-1] <= x:
                stk.pop(-1)
            if stk:
                q[i] = stk[-1]
            else:
                q[i] = -1
            stk.append(x)
            i -= 1
        d = {}
        for k, v in enumerate(nums2):
            d[v] = k
        res = []
        for c in nums1:
            res.append(q[d[c]])
        return res


solution = Solution()
print(solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
print(solution.nextGreaterElement([2, 4], [1, 2, 3, 4]))
