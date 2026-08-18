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

    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        l = 0
        while cur.next:
            l += 1
            cur = cur.next
        cur = dummy
        for i in range(l - n):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next
