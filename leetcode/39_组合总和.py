class Solution:
    def combinationSum(self, nums, target):
        res = []
        path = []

        def dfs(index, target):
            if not target:
                res.append(path[:])
                return
            if index == len(nums):
                return

            i = 0
            while nums[index] * i <= target:
                dfs(index + 1, target - nums[index] * i)
                path.append(nums[index])
                i += 1

            i = 0
            while nums[index] * i <= target:
                path.pop()
                i += 1

        dfs(0, target)
        return res

solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))
print(solution.combinationSum([2, 3, 5], 8))
print(solution.combinationSum([2], 1))
print(solution.combinationSum([1], 1))
print(solution.combinationSum([1], 2))
print(solution.combinationSum([1], 3))
print(solution.combinationSum([1], 4))
print(solution.combinationSum([1], 5))
print(solution.combinationSum([1], 6))
print(solution.combinationSum([1], 7))