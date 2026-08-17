class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        def dfs(node):
            if not node:
                return 0
            cnt = dfs(node.next)
            if cnt == n:
                node.next = node.next.next
            return cnt + 1

        dfs(dummy)
        return dummy.next
