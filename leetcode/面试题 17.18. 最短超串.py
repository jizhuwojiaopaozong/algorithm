from typing import List
from collections import defaultdict


class Solution:
    def shortestSeq(self, l1: List[int], l2: List[int]) -> List[int]:
        h1 = defaultdict(int)
        h2 = defaultdict(int)
        for c in l2:
            h2[c] += 1
        i = 0
        j = 0
        cnt = 0
        res = []
        left = 0
        right = 0
        while i < len(l1):
            h1[l1[i]] += 1
            if h1[l1[i]] <= h2[l1[i]]:
                cnt += 1
            while j < len(l1) and h1[l1[j]] > h2[l1[j]]:
                h1[l1[j]] -= 1
                j += 1
            if cnt == len(l2):
                if not res or i - j + 1 < len(res):
                    res = l1[j : i + 1]
                    left = j
                    right = i
            i += 1
        if res:
            return [left, right]
        else:
            return []

    # 精确匹配，不允许包含多余的元素，变为固定滑动窗口
    def shortestSeq2(self, l1: List[int], l2: List[int]) -> List[int]:
        if len(l1) < len(l2):
            return []
        h2 = defaultdict(int)
        for c in l2:
            h2[c] += 1
        h1 = defaultdict(int)
        for i in range(len(l2)):
            h1[l1[i]] += 1
        if h1 == h2:
            return [0, len(l2) - 1]
        for i in range(len(l2), len(l1)):
            h1[l1[i]] += 1
            h1[l1[i - len(l2)]] -= 1
            if h1[l1[i - len(l2)]] == 0:
                del h1[l1[i - len(l2)]]
            if h1 == h2:
                return [i - len(l2) + 1, i]
        return []

    # 精确匹配，不允许包含多余的元素，变为固定滑动窗口
    def shortestSeq3(self, l1: List[int], l2: List[int]) -> List[int]:
        if not l1 or not l2:
            return []
        if len(l1) < len(l2):
            return []
        h2 = defaultdict(int)
        for c in l2:
            h2[c] += 1
        res = []
        h1 = defaultdict(int)
        left = 0
        valid_num = 0
        for i in range(len(l1)):
            if l1[i] in h2:
                h1[l1[i]] += 1
                valid_num += 1

                while h1[l1[i]] > h2[l1[i]]:
                    h1[l1[left]] -= 1
                    left += 1
                    valid_num -= 1

                if valid_num == len(l2):
                    res.append([left, i])
            else:
                h1.clear()
                valid_num = 0
                left += 1
        return res


sol = Solution()
# print(sol.shortestSeq([7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7], [1, 5, 9]))
# print(sol.shortestSeq([1, 2, 3], [4]))

print(sol.shortestSeq3([1, 5, 5, 9], [1, 5, 9]))
print(sol.shortestSeq3([9, 1, 5, 1, 2, 5, 9], [1, 5, 9]))
