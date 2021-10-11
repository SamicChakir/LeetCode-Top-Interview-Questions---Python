# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right




class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        stack_of_nodes = []

        stack_of_nodes.append(root)

        while len(stack_of_nodes) > 0:
            current = stack_of_nodes.pop()
            stack_of_nodes.append(current)
            while (current.left is not None):
                current = current.left
                stack_of_nodes.append(current)
            res.append(current.val)
            stack_of_nodes.pop()
            if current.right is None:
                if len(stack_of_nodes) > 0:
                    current = stack_of_nodes.pop() #get parent from stack
                    current.left = None
                    stack_of_nodes.append(current)

            else:
                stack_of_nodes.append(current.right)

        return res




    def recurisveTraversal(self, root, l):
        if root is None:
            return l

        l = self.recurisveTraversal(root.left, l)
        l.append(root.val)
        l = self.recurisveTraversal(root.right, l)

        return l



node1 = TreeNode(3)
node2 = TreeNode(2,None,None)
node3 = TreeNode(1,None,node2)


sol = Solution()
print(sol.inorderTraversal(node3))