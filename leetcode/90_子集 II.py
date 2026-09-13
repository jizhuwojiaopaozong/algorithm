from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def dfs(index):
            if index == len(nums):
                res.append(path[:])
                return
            else:
                k = index + 1
                while k < len(nums) and nums[k] == nums[index]:
                    k += 1
                for i in range(k - index + 1):
                    dfs(k)
                    path.append(nums[index])

                for i in range(k - index + 1):
                    path.pop()

        dfs(0)
        return res


s = Solution()
print(s.subsetsWithDup([1, 2, 2]))
print(s.subsetsWithDup([0]))
