# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root.right is None and root.left is None:
            return True

        elif root.right is None:
            return False
        elif root.left is None:
            return True
        else:
            leftTree = self.getInorderTraversalList(root.left)
            rightTree = self.getReverseInOrderTraversalList(root.right)

            if len(leftTree) != len(rightTree):
                return False
            size = len(leftTree)
            for i in range(size):
                if leftTree[i] != rightTree[i]:
                    return False

            return True

    def getInorderTraversalList(self,root):
        if root is None:
            return []
        res = []
        stack_of_nodes = []

        stack_of_nodes.append(root)

        dict_of_source = dict()

        dict_of_source[root] = "Parent"

        while len(stack_of_nodes) > 0:
            current = stack_of_nodes.pop()
            stack_of_nodes.append(current)
            while (current.left is not None):
                current = current.left
                dict_of_source[current] = "Left"
                stack_of_nodes.append(current)
            res.append(str(current.val) + dict_of_source[current])
            stack_of_nodes.pop()
            if current.right is None:
                if len(stack_of_nodes) > 0:
                    current = stack_of_nodes.pop()  # get parent from stack
                    current.left = None
                    stack_of_nodes.append(current)

            else:
                dict_of_source[current.right] = "Right"
                stack_of_nodes.append(current.right)

        return res

    def getReverseInOrderTraversalList(self,root):

        if root is None:
            return []
        res = []
        stack_of_nodes = []

        stack_of_nodes.append(root)

        dict_of_source = dict()

        dict_of_source[root] = "Parent"


        while len(stack_of_nodes) > 0:
            current = stack_of_nodes.pop()
            stack_of_nodes.append(current)
            while (current.right is not None):
                current = current.right
                dict_of_source[current] = "Left"
                stack_of_nodes.append(current)
            res.append(str(current.val) + dict_of_source[current])
            stack_of_nodes.pop()
            if current.left is None:
                if len(stack_of_nodes) > 0:
                    current = stack_of_nodes.pop()  # get parent from stack
                    current.right = None
                    stack_of_nodes.append(current)

            else:
                dict_of_source[current.left] = "Right"
                stack_of_nodes.append(current.left)

        return res


node3Sim = TreeNode(3,None,None)
node4Sim = TreeNode(4,None,None)
node3 = TreeNode(3,None,None)
node4 = TreeNode(4,None,None)
node2 = TreeNode(2,node3,node4)
node2Sim = TreeNode(2,node4Sim,node3Sim)
node1 = TreeNode(1,node2,node2Sim)





sol = Solution()
print(sol.isSymmetric(node1))
