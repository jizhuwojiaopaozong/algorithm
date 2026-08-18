from typing import List


class Solution:
    def kthSmallest(self, matrixs: List[List[int]], k: int) -> int:
        l = matrixs[0][0]
        r = matrixs[-1][-1]
        while l < r:
            mid = (l + r) // 2
            n = 0
            j = len(matrixs[0]) - 1
            for i in range(len(matrixs)):
                while j >= 0 and matrixs[i][j] > mid:
                    j -= 1
                n += j + 1
            # 注意不能写成N<=k，这样是寻找最后一个满足条件的值（右边界），实际上是N>=K，即寻找第一个满足条件的值，左边界。
            if n >= k:
                r = mid
            else:
                l = mid + 1
        return l


sol = Solution()
print(sol.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
print(sol.kthSmallest([[-5]], 1))
