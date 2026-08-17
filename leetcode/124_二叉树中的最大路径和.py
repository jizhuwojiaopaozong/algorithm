from queue import Queue


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode):
        ans = float("-inf")
        path = []

        def dfs(root):
            nonlocal ans, path
            if not root:
                return 0, []

            left, l_path = dfs(root.left)
            right, r_path = dfs(root.right)
            if left < 0:
                left = 0
                l_path = []
            if right < 0:
                right = 0
                r_path = []
            if left + right + root.val > ans:
                ans = left + right + root.val
                path = l_path + [root.val] + r_path
            if left > right:
                return left + root.val, [root.val] + l_path
            else:
                return right + root.val, [root.val] + r_path

        dfs(root)
        return ans, path

    def createtreeNode(self, nums):
        if not nums or len(nums) == 0:
            return None
        root = TreeNode(nums[0])
        q = Queue()
        q.put(root)
        i = 1
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


sol = Solution()
nums = [1, 2, 3, 4, 5]
root = sol.createtreeNode(nums)
print(sol.maxPathSum(root))


nums = [1, 2, 3]
root = sol.createtreeNode(nums)
print(sol.maxPathSum(root))


nums = [-10, 9, 20, None, None, 15, 7]
root = sol.createtreeNode(nums)
print(sol.maxPathSum(root))
