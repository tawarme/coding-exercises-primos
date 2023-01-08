# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverser(self, head, prev):
        if head.next is not None:
            new_head = self.reverser(head.next, head)
        else:
            new_head = head
        head.next = prev
        print("hi")

    def reverseList(self, head):
        
        new_head = self.reverser(head, None)

        return new_head

def link_generator(lister):
    if not lister:
        return None
    prev_node = ListNode(lister[0], None)
    head = None
    for item in lister[1:]:
        head = ListNode(item, prev_node)
        prev_node = head

    #print(head.val, head.next.val)
    return head

def link_printer(head):

    while head is not None:
        print(head.val)
        head = head.next

# link = link_generator([1,2,3,4,5])
link = link_generator([5,4,3,2,1])

link_printer(link)

print(Solution().reverseList(link))
