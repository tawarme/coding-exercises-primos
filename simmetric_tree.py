# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def go(self, p, q):
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            if bool(p.right) == bool(q.left):
                same = self.go(p.right, q.left)
                if not same: 
                    return False
            else:
                return False
            if bool(p.left) == bool(q.right):
                same = self.go(p.left, q.right)        
                if not same:
                    return False
            else:
                return False
        else:
            return False

        return True


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        p = root.right
        q = root.left

        if not p and not q:
            return True

        if p and q:
            return self.go(p, q)
        else:
            return False

