class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        while p.next:
            q = p.next.next
            while q and q.val == p.next.val:
                q = q.next
            if p.next.next == q:
                p = p.next
            else:
                p.next = q
        return dummy.next

    def createListNode(self, nums) -> ListNode:
        if len(nums) == 0:
            return None
        head = ListNode(nums[0])
        cur = head
        for i in nums[1:]:
            cur.next = ListNode(i)
            cur = cur.next
        return head

    def printListNode(self, head):
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res


sol = Solution()
head = sol.createListNode([1, 2, 3, 4, 5])
ans = sol.deleteDuplicates(head)
print(sol.printListNode(ans))

head = sol.createListNode([1, 2, 3, 3, 4, 4, 5])
ans = sol.deleteDuplicates(head)
print(sol.printListNode(ans))

head = sol.createListNode([1, 1, 1, 2, 3])
ans = sol.deleteDuplicates(head)
print(sol.printListNode(ans))
