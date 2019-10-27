class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == "" or needle == haystack:
            return 0
        
        i = 0
        right = len(needle)
        
        while i <= (len(haystack)-right):
            if needle == haystack[i:i+right]:
                return i
            else:
                i+=1
        
        return -1