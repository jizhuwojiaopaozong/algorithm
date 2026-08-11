from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def dfs(u, k, path):
            if u == len(s) and k == 4:
                ans.append(path[:-1])
                return
            if u == len(s) or k == 4:
                return
            t = 0
            for i in range(u, len(s)):
                if i > u and s[u] == '0':
                    break
                t = t * 10 + int(s[i])
                if t > 255:
                    break
                else:
                    dfs(i + 1, k + 1, path + str(t) + ".")

        dfs(0, 0, "")
        return ans


sol = Solution()
print(sol.restoreIpAddresses("25525511135"))
print(sol.restoreIpAddresses("0000"))
print(sol.restoreIpAddresses("101023"))
