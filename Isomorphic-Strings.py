class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        compare = {}

        for i in range(len(s)):
            if s[i] not in compare:
                if t[i] not in compare.values():
                    compare[s[i]] = t[i]
                else:
                    return False
            else:
                if t[i] != compare[s[i]]:
                    return(False)
                else:
                    continue

        return(True)