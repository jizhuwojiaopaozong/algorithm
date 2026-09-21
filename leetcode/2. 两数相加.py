from typing import List


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        t = 0
        while l1 or l2 or t:
            if l1:
                t += l1.val
                l1 = l1.next
            if l2:
                t += l2.val
                l2 = l2.next
            cur.next = ListNode(t % 10)
            t //= 10
            cur = cur.next
        cur.next = None
        return dummy.next

    def createListNode(self, nums: List[int]) -> ListNode:
        if not nums or len(nums) == 0:
            return None
        head = ListNode(nums[0])
        cur = head
        for c in nums[1:]:
            cur.next = ListNode(c)
            cur = cur.next
        cur.next = None
        return head

    def printListNode(self, head: ListNode) -> List[int]:
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res


sol = Solution()
head1 = sol.createListNode([2, 4, 3])
head2 = sol.createListNode([5, 6, 4])
ans = sol.addTwoNumbers(head1, head2)
print(sol.printListNode(ans))

head1 = sol.createListNode([0])
head2 = sol.createListNode([0])
ans = sol.addTwoNumbers(head1, head2)
print(sol.printListNode(ans))

head1 = sol.createListNode([9, 9, 9, 9, 9, 9, 9])
head2 = sol.createListNode([9, 9, 9, 9])
ans = sol.addTwoNumbers(head1, head2)
print(sol.printListNode(ans))
