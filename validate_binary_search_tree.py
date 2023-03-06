# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = float("-inf")
    
    def go(self, root):
        if root.left:
            if not self.go(root.left):
                return False

        if not self.prev < root.val:
            return False

        self.prev = root.val            

        if root.right:
            if not self.go(root.right):
                return False

        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.go(root)
