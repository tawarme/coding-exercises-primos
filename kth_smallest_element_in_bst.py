# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    i = 1
    ans = None

    def go(self, root, k):
        if root.left:
            ans = self.go(root.left, k)
            if ans is not None:
                return ans

        if k == self.i:
            return root.val
        
        self.i += 1

        if root.right:
            ans = self.go(root.right, k)

            if ans is not None:
                return ans


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.go(root, k)
