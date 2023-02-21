# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_sum = None

    def go(self, root, max_sum):
        #if root is None:
        #    return 0
            #return float("-inf")

        local_max = root.val
        local_sum = root.val

        if root.left is not None:
            leftmax = self.go(root.left, self.max_sum)
            self.max_sum = max(self.max_sum, leftmax)
            local_max = max(local_max, root.val+leftmax)
            local_sum += leftmax

        if root.right is not None:
            rightmax = self.go(root.right, self.max_sum)
            self.max_sum = max(self.max_sum, rightmax)
            local_max = max(local_max, root.val+rightmax)
            local_sum += rightmax

        #if root.left is not None and root.right is not None:
        #self.max_sum = max(self.max_sum, root.val+leftmax+rightmax)
        self.max_sum = max(self.max_sum, local_sum)

        #local_max = max(root.val, root.val+leftmax, root.val+rightmax)

        return local_max

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        self.max_sum = root.val

        dummy = TreeNode(0, root)

        self.go(dummy, self.max_sum)
        #return max(self.max_sum, root.val + self.go(root, self.max_sum))
        return self.max_sum
