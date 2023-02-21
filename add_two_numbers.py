# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        dummy = ListNode()
        prev = dummy

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            cur_val = v1 + v2 + carry

            carry = cur_val // 10
            cur = ListNode(cur_val % 10)

            prev.next = cur
            prev = cur

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
