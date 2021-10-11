
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        dictionaryValuePerLevel = self.recursiveZigzagLevelTraversal(root, dict(), 0)


        return root

    def recursiveZigzagLevelTraversal(self,root,dictio,level):
        if root is None:
            return dictio
        if level in dictio:
            dictio[level][-1].next = root
            dictio[level].append(root)
        else:
            dictio[level] = [root]

        dictio = self.recursiveZigzagLevelTraversal(root.left,dictio,level +1)
        dictio = self.recursiveZigzagLevelTraversal(root.right,dictio,level +1)

        return dictio
