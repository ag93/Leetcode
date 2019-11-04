class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        prev_root = None
        
        for item in preorder:
            if prev_root and item < prev_root:
                return False
            
            while stack and item > stack[-1]:
                prev_root = stack.pop()
                
            stack.append(item)
            
        return True