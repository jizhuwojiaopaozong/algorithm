from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stk = []
        res = []
        while root or stk:
            while root:
                res.append(root.val)
                stk.append(root)
                root = root.right
            root = stk[-1].left
            stk.pop(-1)
        return res[::-1]

    def postorderTraversal_dfs(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)

        dfs(root)
        return res
