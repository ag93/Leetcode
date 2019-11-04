# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        total = 0
        stack = [root]
        while stack:
            temp = stack.pop()

            if temp.left and not temp.left.left and not temp.left.right:
                total += temp.left.val
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
                
        return total