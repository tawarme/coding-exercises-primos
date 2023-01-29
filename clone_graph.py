"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def go(self, node, checked):
        #print("Checking node", node.val)
        checked[node.val] = Node(node.val)

        for nei in node.neighbors:
            if not checked.get(nei.val):
                self.go(nei, checked)
            #print(checked)
            checked[node.val].neighbors.append(checked[nei.val])

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None

        checked = {}

        self.go(node, checked)

        return checked[1]
