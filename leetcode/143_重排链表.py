class LinkNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Solution:
    def reorderList(self, head: LinkNode) -> LinkNode:
        p = head
        n = 1
        while p.next:
            p = p.next
            n += 1
        mid = head
        for _ in range(n // 2):
            mid = mid.next
        if n % 2:
            tmp = n // 2
        else:
            tmp = n // 2 - 1
        p = mid
        q = mid.next
        for _ in range(tmp):
            r = q.next
            q.next = p
            p = q
            q = r
        tail = p
        p = head
        for _ in range(tmp):
            o = tail.next
            tail.next = p.next
            p.next = tail
            p = tail.next
            tail = o
        tail.next = None
        return head
