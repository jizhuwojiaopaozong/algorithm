from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = [-100] * len(nums)
        state = [False] * len(nums)

        def dfs(index):
            if index == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not state[i]:
                    path[index] = nums[i]
                    state[i] = True
                    dfs(index + 1)
                    state[i] = False
                    path[index] = -100

        dfs(0)

        return res


solution = Solution()
print(solution.permute([1, 2, 3]))
print(solution.permute([0, 1]))
print(solution.permute([1]))