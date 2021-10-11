# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root.left is None and root.right is None:
            return root.val

        res = []
        stack_of_nodes = []

        stack_of_nodes.append(root)

        while len(stack_of_nodes) > 0:
            if len(res) == k :
                break
            current = stack_of_nodes.pop()
            stack_of_nodes.append(current)
            while (current.left is not None):
                current = current.left
                stack_of_nodes.append(current)
            res.append(current.val)
            stack_of_nodes.pop()
            if current.right is None:
                if len(stack_of_nodes) > 0:
                    current = stack_of_nodes.pop()  # get parent from stack
                    current.left = None
                    stack_of_nodes.append(current)

            else:
                stack_of_nodes.append(current.right)

        return res[-1]