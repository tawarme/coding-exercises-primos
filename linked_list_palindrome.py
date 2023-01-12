# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        prev = None
        fast = head
        #x =0
        while head is not None:
            #print("iter", x)
            #x+=1
            if not fast:
                # prev has the reversed pointer
                # head has middle pointer
                #print("reversed pointer", prev.val) # if pair, right
                #print("middle pointer", head.val) # if pair left
                if prev.val != head.val:
                    return False
                else:
                    prev = prev.next
                    head = head.next
            else:
                #print("head moving", head.val)
                if fast.next:
                    fast = fast.next.next
                    mem = head.next
                    head.next = prev
                    prev = head
                    head = mem  #head is now " .next"
                else:
                    fast = None
                    mem = head.next
                    head.next = prev
                    prev = head
                    head = mem #head is now " .next"
                    prev = prev.next
                #fast = fast.next.next
                

        return True
