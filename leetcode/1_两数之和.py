from typing import List
from collections import defaultdict

class Solution:
    ## 暴力枚举
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]
    
    ## 哈希表
    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in d:
                return [d[tmp], i]
            d[nums[i]] = i
        return [-1, -1]
    
    ## 两数之和 变形题（数组有重复数字，需要输出所有符合要求的数字对）（https://juejin.cn/post/7337225888265338934）
    ## 输入：[3, 3, 3, 4, 2, 3], 6
    ## 输出：[[3, 3], [3, 3], [3, 3], [4, 2], [3, 3], [3, 3], [3, 3]]
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        d = defaultdict(list)
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in d:
                for ii in d[tmp]:
                    res.append([nums[ii], nums[i]])
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]] = [i]
        return res

    def twoSum_3(self, nums: List[int], target: int) -> List[List[int]]:
        # 2, 3, 3, 3, 3, 4
        nums.sort()
        res = []
        i = 0
        j = len(nums) - 1
        while i < j:
            while i < j - 1 and nums[i] + nums[j-1] >= target:
                j -= 1
            if nums[i] + nums[j] == target:
                res.append([nums[i], nums[j]])
            i += 1
        return res
    
solution = Solution()
print(solution.twoSum_3([3, 3, 3, 4, 2, 3], 6))
# print(solution.twoSum_1([3, 2, 4], 6))