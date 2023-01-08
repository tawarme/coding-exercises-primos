class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        while fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                return True
