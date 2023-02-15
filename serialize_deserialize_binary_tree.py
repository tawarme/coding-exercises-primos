# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ordered = []
        stack = [root]

        while stack:
            node = stack.pop(0)

            if node is not None:
                #lev_not_null = True
                ordered.append(str(node.val))

                stack.append(node.left)
                stack.append(node.right)
            else:
                ordered.append("None")

        return ",".join(ordered)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        node_vals = data.split(",")
        stack = []

        dummy = TreeNode()

        prev_node = dummy
        for i in range(len(node_vals)):
            #print(i, stack, "prev", prev_node)
            val = node_vals[i]

            node = None

            if val != "None":
                val = int(val)

                node = TreeNode(val)

                stack.append(node)

            if not i % 2 == 0:
                prev_node.left = node
            else:
                prev_node.right = node

                if not stack:
                    break

                prev_node = stack.pop(0)

        return dummy.right

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
