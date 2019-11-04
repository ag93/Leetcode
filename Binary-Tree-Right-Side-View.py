# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        levels = []
        answer = []
        level = 0
        queue = [root]
        
        while queue:
            levels.append([])

            for i in range(len(queue)):
                node = queue.pop(0)
                levels[level].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
            
        for i in levels:
            answer.append(i[-1])
        
        return answer