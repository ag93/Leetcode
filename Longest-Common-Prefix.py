class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            while(strs[i].startswith(prefix) == 0):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                
        return prefix