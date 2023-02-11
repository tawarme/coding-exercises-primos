# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:


        # prev--->head--->next
        # prev<---head

        dummy = ListNode()

        prev = None
        psegment_tail = dummy
        segment_tail = None
        segment_count = 0

        while head:
            if segment_count == 0:
                segment_tail = head

            mem = head.next
            head.next = prev
            
            segment_count += 1
            
            if segment_count == k:
                psegment_tail.next = head
                psegment_tail = segment_tail
                prev = None
                segment_count = 0
            else:
                prev = head

            head = mem

        if 0 < segment_count < k:
            # reverse prev
            nprev = None
            nhead = prev

            while nhead:
                nmem = nhead.next
                nhead.next = nprev

                nprev = nhead
                nhead = nmem

            psegment_tail.next = nprev


        return dummy.next
