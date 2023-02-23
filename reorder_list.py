# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            #if not fast.next:
                # Allow slow to be kicked one place
            #    print("HERE")
            #    break
            fast = fast.next.next

        if fast:
            slow = slow.next

        # at the middle
        #print(slow)

        rev_head = slow
        prev = None


        #prev ---> rev_head --->next
        #prev<----rev_head
        while rev_head:
            mem = rev_head.next
            rev_head.next = prev

            prev = rev_head
            rev_head = mem

        orig_head = head

        mid = prev
        dummy = ListNode()
        prev = dummy

        #print(mid)
        while head and prev:
            hnext = head.next
            mnext = mid.next if mid else None

            prev.next = head
            head.next = mid

            prev = mid
            head = hnext
            mid = mnext

        return dummy.next

        