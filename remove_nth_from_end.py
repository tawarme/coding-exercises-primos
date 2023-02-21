0/5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def go(self, head, prev, n):
        if not head:
            return 1

        cur_i = self.go(head.next, head, n)

        if cur_i == n and prev:
            prev.next = head.next

        return cur_i + 1


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        count = self.go(head, None, n)
        
        if count -1 == n:
            return head.next

        return head
