from typing import List
from queue import Queue


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = Queue()
        if root:
            q.put(root)
        res = []
        while not q.empty():
            ans = []
            size = q.qsize()
            while size:
                size -= 1
                tmp = q.get()
                ans.append(tmp.val)
                if tmp.left:
                    q.put(tmp.left)
                if tmp.right:
                    q.put(tmp.right)
            res.append(ans)
        return res

    def levelOrder_dfs(self, root: TreeNode) -> List[List[int]]:
        res = []

        def dfs(node, level):
            if not node:
                return
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return res

    def createTreeNode(self, nums):
        if nums is None or len(nums) == 0:
            return None
        root = TreeNode(nums[0])
        i = 1
        q = Queue()
        q.put(root)
        while not q.empty() and i < len(nums):
            size = q.qsize()
            while size:
                size -= 1
                tmp = q.get()
                if i < len(nums) and nums[i] is not None:
                    tmp.left = TreeNode(nums[i])
                    q.put(tmp.left)
                i += 1
                if i < len(nums) and nums[i] is not None:
                    tmp.right = TreeNode(nums[i])
                    q.put(tmp.right)
                i += 1
        return root


solution = Solution()
# root = solution.createTreeNode([3, 9, 20, None, None, 15, 7])
# print(solution.levelOrder(root))

# root = solution.createTreeNode([1])
# print(solution.levelOrder(root))

root = solution.createTreeNode([])
print(solution.levelOrder(root))
