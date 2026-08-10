class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        cur = head
        p = head.next
        while p:
            if p.val != cur.val:
                cur.next = p
                cur = p
            p = p.next
        cur.next = None
        return head
