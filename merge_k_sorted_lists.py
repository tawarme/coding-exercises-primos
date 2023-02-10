from queue import PriorityQueue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = PriorityQueue()

        for head in lists:
            while head:
                heap.put(head.val)

                head = head.next

        dummy = ListNode(None, None)
        new_head = dummy

        while not heap.empty():
            node = ListNode(heap.get())
            new_head.next = node

            new_head = new_head.next

        return dummy.next
