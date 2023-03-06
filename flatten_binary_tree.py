# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def go(self, root):
        if not root:
            return None

        if not root.left and not root.right:
            return root

        llast = self.go(root.left)
        llast = llast if llast else root.left

        rlast = self.go(root.right)
        rlast = rlast if rlast else root.right

        mright = root.right

        if root.left:
            root.right = root.left

            llast.right = mright
            root.left = None

        return rlast if rlast else llast

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        self.go(root)