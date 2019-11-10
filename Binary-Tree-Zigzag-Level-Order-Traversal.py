class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        l_2_r = True
        if not root:
            return
        
        queue = []
        queue.append(root)
        result = []
        while queue:
            length = len(queue)
            current_res = []
            for _ in range(length):
                if l_2_r:
                    current = queue.pop(0)
                    current_res.append(current.val)
                    if current.left: queue.append(current.left)
                    if current.right: queue.append(current.right)
                else:
                    current = queue.pop()
                    current_res.append(current.val)
                    if current.right: queue.insert(0,current.right)
                    if current.left: queue.insert(0,current.left)
            result.append(current_res)
            l_2_r = not l_2_r
        return result