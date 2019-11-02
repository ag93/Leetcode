class Solution:
    def lastSubstring(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        current = s[-1]
        for i in range(len(s)-2, -1, -1):
            check = s[i:]
            if check > current:
                current = check
                
        return(current)