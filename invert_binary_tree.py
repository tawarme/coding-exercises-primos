# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def go(self, root):
        #print(root.right.val, root.left.val, "BEFORE")
        mem = root.right
        root.right = root.left
        root.left = mem
        #print(root.right.val, root.left.val, "AFTER")

        if root.right:
            self.go(root.right)
        if root.left:
            self.go(root.left)


    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return None

        self.go(root)

        return root
