def wordPattern(pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        patternDict = {}
        sList = s.split(" ")

        if(len(sList) != len(pattern)):
            return False

        for i in range(len(sList)):
            if sList[i] not in patternDict.keys() and pattern[i] not in patternDict.values():
                patternDict[sList[i]] = pattern[i]

        resultPattern = ""
        for s in sList:
            if s not in patternDict:
                return False
            else:
                resultPattern += patternDict[s]

        return resultPattern == pattern

if __name__ == "__main__":
    pattern = "aba"
    s = "dog cat dog"
    print(wordPattern(pattern, s))