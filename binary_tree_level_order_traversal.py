# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        q = [root]
        ans = []
        levels = {root:0}

        top_lev = 0
        while q:
            node = q.pop(0)
            lev = levels[node]

            top_lev = max(top_lev, lev)

            if node.left:
                q.append(node.left)
                levels[node.left] = lev +1
            
            if node.right:
                q.append(node.right)
                levels[node.right] = lev +1


        ans = [[] for level in range(top_lev+1)]
        for node, lev in levels.items():
            ans[lev].append(node.val)


        return ans
