import heapq
from typing import List


class LinkNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[LinkNode]) -> LinkNode:
        dummy = LinkNode(-1)
        cur = dummy
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i))
        while heap:
            val, i = heapq.heappop(heap)
            cur.next = lists[i]
            cur = lists[i]
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        return dummy.next


    def createLinkNode(self, nums: List[int]) -> LinkNode:
        if len(nums) == 0:
            return None
        head = LinkNode(nums[0])
        cur = head
        for i in nums[1:]:
            cur.next = LinkNode(i)
            cur = cur.next
        return head

    def prinLinkNode(self, head: LinkNode):
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res)


solution = Solution()
# l1 = solution.createLinkNode([1, 4, 5])
# l2 = solution.createLinkNode([1, 3, 4])
# l3 = solution.createLinkNode([2, 6])
# ans = solution.mergeKLists([l1, l2, l3])
# solution.prinLinkNode(ans)

# ans = solution.mergeKLists([])
# solution.prinLinkNode(ans)

ans = solution.mergeKLists([[]])
solution.prinLinkNode(ans)