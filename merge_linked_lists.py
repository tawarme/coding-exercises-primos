# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from reverse_linked_list import link_generator, link_printer

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None and list2 is None:
            return

        if list2 is None or (list1 is not None and (list1.val < list2.val)):
            path = list1
            other_list = list2
        else:
            path = list2
            other_list = list1
        path_pointer = path

        while path_pointer.next is not None or other_list is not None:
            if path_pointer.next is None or (other_list is not None and other_list.val < path_pointer.next.val): 
                helper = path_pointer.next
                path_pointer.next = other_list
                other_list = helper
            path_pointer = path_pointer.next
                
        return path

list2 = link_generator([1,3,4])
list1 = link_generator([1,2,4])
#list2 = link_generator([])
#list1 = link_generator([])

link_printer(Solution().mergeTwoLists(list1, list2))
