from typing import List


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
            if slow == fast:
                return True
        return False

    def createListNode(self, nums: List[int], pos: int) -> ListNode:
        if len(nums) == 0:
            return None
        head = ListNode(nums[0])
        cur = head
        pos_node = None
        if pos == 0:
            pos_node = head
        for i in nums[1:]:
            cur.next = ListNode(i)
            cur = cur.next
            if pos > 0:
                pos_node = cur
                pos -= 1
        cur.next = pos_node
        return head


solution = Solution()
nums = [3, 2, 0, -4]
pos = 1
head = solution.createListNode(nums, pos)
print(solution.hasCycle(head))
nums = [1,2]
pos = 0
head = solution.createListNode(nums, pos)
print(solution.hasCycle(head))
nums = [1]
pos = -1
head = solution.createListNode(nums, pos)
print(solution.hasCycle(head))
