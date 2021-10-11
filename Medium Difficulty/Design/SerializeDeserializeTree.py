#Definition for a binary tree node.
from queue import Queue
class TreeNode(object):
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        Tree_string = ""
        if root is None:
            return Tree_string

        queue_of_nodes = Queue()
        queue_of_nodes.put(root)

        while (queue_of_nodes.qsize()):
            current = queue_of_nodes.get()
            if current is None:
                Tree_string += ",null"
                continue
            else:
                Tree_string += "," + str(current.val)
            queue_of_nodes.put(current.left)
            queue_of_nodes.put(current.right)

        return Tree_string[1:]


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        splitData = data.split(",")
        if len(splitData) == 1:
            return None
        root = TreeNode(splitData.pop(0))
        queue_of_nodes = Queue()
        queue_of_nodes.put(root)
        while queue_of_nodes.qsize() > 0:
            current = queue_of_nodes.get()
            left_val = splitData.pop(0)
            if left_val != "null":
                leftNode = TreeNode(left_val)
                current.left = leftNode
                queue_of_nodes.put(leftNode)
            right_val = splitData.pop(0)
            if right_val != "null":
                rightNode = TreeNode(right_val)
                current.right = rightNode
                queue_of_nodes.put(rightNode)
        return root




node4 = TreeNode(4,None,None)
node5 = TreeNode(5,None,None)
node2 = TreeNode(2,None,None)
node3 = TreeNode(3,node4,node5)
node1 = TreeNode(1,node2,node3)



sol = Codec()
data = sol.serialize(node1)
sol.deserialize(data)
