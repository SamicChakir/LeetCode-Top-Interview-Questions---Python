# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dictionaryValuePerLevel = self.recursiveZigzagLevelTraversal(root,dict(),0)
        res = []
        levels = len(dictionaryValuePerLevel)

        for i in range(levels):
            if i%2 == 0:
                res.append(dictionaryValuePerLevel[i])
            else:
                dictionaryValuePerLevel[i].reverse()
                res.append(dictionaryValuePerLevel[i])

        return res


    def recursiveZigzagLevelTraversal(self,root,dictio,level):
        if root is None:
            return dictio
        if level in dictio:
            dictio[level].append(root.val)
        else:
            dictio[level] = [root.val]

        dictio = self.recursiveZigzagLevelTraversal(root.left,dictio,level +1)
        dictio = self.recursiveZigzagLevelTraversal(root.right,dictio,level +1)

        return dictio



node1 = TreeNode(3)
node7 = TreeNode(7,None,None)
node15 = TreeNode(15,None,None)
node20 = TreeNode(20,node15,node7)
node9 = TreeNode(9,None,None)
node3 = TreeNode(3,node9,node20)


sol = Solution()
print(sol.zigzagLevelOrder(node3))