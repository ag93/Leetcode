class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1
        
        for i in range(len(s)-1):
            if s[i] not in s[i+1:] and s[i] not in s[:i]:
                return i
            
        if s[-1] not in s[:-1]:
            return len(s)-1
            
        return -1