class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for s in strs:
            word = ''.join(sorted(s))
            if word not in anagrams:
                anagrams[word] = [s]
            else:
                anagrams[word].append(s)                    
        return list(anagrams.values())