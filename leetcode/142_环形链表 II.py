from typing import List


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow = head
        fast = head.next
        while fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
            if fast == slow:
                slow = head
                fast = fast.next
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

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

    def detectCycleCount(self, head: ListNode) -> int:
        if not head or not head.next:
            return 0
        slow = head
        fast = head.next
        while fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                return 0
            fast = fast.next
            if fast == slow:
                slow = head
                fast = fast.next
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                cnt = 1
                while fast.next != slow:
                    cnt += 1
                    fast = fast.next
                return cnt
        return 0
                

solution = Solution()
nums = [3, 2, 0, -4]
pos = 1
head = solution.createListNode(nums, pos)
# print(solution.detectCycle(head).value)
print(solution.detectCycleCount(head))

nums = [3, 2, 0, -4]
pos = 3
head = solution.createListNode(nums, pos)
# print(solution.detectCycle(head).value)
print(solution.detectCycleCount(head))


nums = [3, 2, 0, -4]
pos = 0
head = solution.createListNode(nums, pos)
# print(solution.detectCycle(head).value)
print(solution.detectCycleCount(head))


nums = [1, 2]
pos = 0
head = solution.createListNode(nums, pos)
# print(solution.detectCycle(head).value)
print(solution.detectCycleCount(head))

nums = [1]
pos = -1
head = solution.createListNode(nums, pos)
# print(solution.detectCycle(head).value)
print(solution.detectCycleCount(head))

nums = [1]
pos = 0
head = solution.createListNode(nums, pos)
# print(solution.detectCycle(head).value)
print(solution.detectCycleCount(head))

