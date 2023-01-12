# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def go(self, root, prev, max):
        left_max = 0
        right_max = 0

        if root.left:
            left_max = self.go(root.left, root, max + 1)
            #print(root.val, "left max is", left_max)
        if root.right:
            right_max = self.go(root.right, root, max + 1)
            #print(root.val, "right max is", right_max)
        
        leafs_max = left_max if left_max > right_max else right_max
        return leafs_max +1


    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        max = 0
        prev = None

        max = self.go(root, prev, max)

        return max
