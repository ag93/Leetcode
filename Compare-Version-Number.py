class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        if version1.count(".") == 0 and version2.count(".") == 0:
            if int(version1) == int(version2):
                return 0
            elif int(version1) > int(version2):
                return 1
            else:
                return -1
        
        
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        var = ""
        
        if len(v1)<len(v2):
            var = v2
        elif len(v1)>len(v2):
            var = v1
        
        itr = min(len(v1), len(v2))
        
        for i in range (itr):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            
        for i in range(itr, len(var)):
            if var == v1 and int(var[i]) != 0:
                return 1
            elif var == v2 and int(var[i]) != 0:
                return -1
            
        return 0