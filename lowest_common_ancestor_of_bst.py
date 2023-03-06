# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def go(self, root, p, q):
        if p <= root.val <= q:
            return root

        if q < root.val:
            return self.go(root.left, p, q)
        else:
            return self.go(root.right, p, q)



    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not p.val < q.val:
            p, q = q, p

        return self.go(root, p.val, q.val)
