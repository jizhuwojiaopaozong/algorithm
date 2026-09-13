from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for i in range(2**n):
            tmp = []
            for j in range(n):
                if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res

    def subsets_dfs(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(index):
            if index == len(nums):
                res.append(path[:])
                return
            else:
                for _ in range(2):
                    dfs(index + 1)
                    path.append(nums[index])
                for _ in range(2):
                    path.pop()

        dfs(0)
        return res


sol = Solution()
print(sol.subsets([1, 2, 3]))
print(sol.subsets([0]))
