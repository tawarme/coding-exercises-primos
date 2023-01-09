class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head

        while fast is not None:
            if fast.next is None:
                return slow
            fast = fast.next.next
            slow = slow.next

        return slow
