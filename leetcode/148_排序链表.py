from typing import List


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList_dfs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortList_dfs(head)
        right = self.sortList_dfs(mid)

        def merge(left, right):
            dummy = ListNode(-1)
            cur = dummy
            while left and right:
                if left.val <= right.val:
                    cur.next = left
                    cur = left
                    left = left.next
                else:
                    cur.next = right
                    cur = right
                    right = right.next
            if left:
                cur.next = left
            else:
                cur.next = right
            return dummy.next

        return merge(left, right)

    def sortList(self, head: ListNode) -> ListNode:
        ln = 0
        p = head
        while p:
            ln += 1
            p = p.next
        i = 1
        while i < ln:
            dummy = ListNode(-1)
            cur = dummy
            for j in range(0, ln, 2 * i):
                p = head
                q = p
                m = 0
                while m < i and q:
                    q = q.next
                    m += 1
                o = q
                n = 0
                while n < i and o:
                    o = o.next
                    n += 1
                l = 0
                r = 0
                while l < i and r < i and p and q:
                    if p.val <= q.val:
                        cur.next = p
                        cur = p
                        p = p.next
                        l += 1
                    else:
                        cur.next = q
                        cur = q
                        q = q.next
                        r += 1
                while l < i and p:
                    cur.next = p
                    cur = p
                    p = p.next
                    l += 1
                while r < i and q:
                    cur.next = q
                    cur = q
                    q = q.next
                    r += 1
                cur.next = None
                head = o
            head = dummy.next
            i *= 2
        return head

    def createListNode(self, nums: List[int]) -> ListNode:
        if len(nums) == 0:
            return None
        head = ListNode(nums[0])
        cur = head
        for i in nums[1:]:
            cur.next = ListNode(i)
            cur = cur.next
        cur.next = None
        return head

    def printListNode(self, head: ListNode):
        res = []
        p = head
        while p:
            res.append(p.val)
            p = p.next
        return res


sol = Solution()
nums = [4, 2, 1, 3]
head = sol.createListNode(nums)
print(sol.printListNode(head))
# head = sol.sortList(head)
head = sol.sortList_dfs(head)
print(sol.printListNode(head))


nums = [-1, 5, 3, 4, 0]
head = sol.createListNode(nums)
print(sol.printListNode(head))
# head = sol.sortList(head)
head = sol.sortList_dfs(head)
print(sol.printListNode(head))


nums = []
head = sol.createListNode(nums)
print(sol.printListNode(head))
# head = sol.sortList(head)
head = sol.sortList_dfs(head)
print(sol.printListNode(head))
