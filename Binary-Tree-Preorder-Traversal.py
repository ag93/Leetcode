# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def preOrder(rootNode):
            if rootNode:
                result.append(rootNode.val)
                preOrder(rootNode.left)
                preOrder(rootNode.right)
        
        preOrder(root)      
        return result