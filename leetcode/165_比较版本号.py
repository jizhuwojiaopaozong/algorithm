from typing import List
from functools import cmp_to_key


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i = 0
        j = 0
        while i < len(version1) or j < len(version2):
            a = i
            b = j
            while a < len(version1) and version1[a] != ".":
                a += 1
            while b < len(version2) and version2[b] != ".":
                b += 1
            if a == i:
                num1 = 0
            else:
                num1 = int(version1[i:a])
            if b == j:
                num2 = 0
            else:
                num2 = int(version2[j:b])
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            i = a + 1
            j = b + 1
        return 0

    def sortCompaerVersion(self, versions: List[str]) -> List[str]:
        return sorted(versions, key=cmp_to_key(self.compareVersion))


sol = Solution()
print(sol.compareVersion("1.01", "1.001"))  # 0
print(sol.compareVersion("1.2", "1.10"))  # -1
print(sol.compareVersion("1.0", "1.0.0.0"))  # 0
print(sol.sortCompaerVersion(["1.01", "1.001", "1.2", "1.10", "1.0", "1.0.0.0"]))