from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = [-100] * len(nums)
        state = [False] * len(nums)

        def dfs(index):
            if index == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not state[i]:
                    if i and nums[i] == nums[i - 1] and not state[i - 1]:
                        continue
                    path[index] = nums[i]
                    state[i] = True
                    dfs(index + 1)
                    state[i] = False
                    path[index] = -100

        dfs(0)
        return res

solution = Solution()
print(solution.permuteUnique([1, 1, 2]))
print(solution.permuteUnique([1, 2, 3]))
print(solution.permuteUnique([0, 1]))
print(solution.permuteUnique([1]))