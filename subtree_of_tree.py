# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def go_compare(self, p, q):
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            if self.go_compare(p.right, q.right):
                if self.go_compare(p.left, q.left):
                    return True

        return False

    def go(self, root, subroot):
        if not root:
            return False
        if root and root.val == subroot.val:
            if self.go_compare(root, subroot):
                return True
        
        if root.right:
            is_subtree = self.go(root.right, subroot)
            if is_subtree:
                return True
        if root.left:
            is_subtree = self.go(root.left, subroot)
            if is_subtree:
                return True
        


    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        return self.go(root, subRoot)
