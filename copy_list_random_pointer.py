"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        orighead = head
        newhead = Node(head.val, None, None)

        prev = head
        newprev = newhead

        orignodes = {head: newhead}
        head = head.next
        while head is not None:
            node = Node(head.val, None, None)
            newprev.next = node

            orignodes[head] = node

            #if prev.random is not None:
            #    nodes[prev.random.val] = nodes.get(prev.random, Node(prev.random.val, None, None))
            #    newprev.random = nodes[prev.random.val]

            newprev = node
            prev = head
            head = head.next

        newcurrent = newhead
        while orighead is not None:
            if orighead.random is not None:
                newcurrent.random = orignodes[orighead.random]

            orighead = orighead.next
            newcurrent = newcurrent.next

        return newhead
