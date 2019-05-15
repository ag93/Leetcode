class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        anagram_index = []
        for i in A:
            ind = B.index(i)
            anagram_index.append(ind)
            B[ind] = ''

        return(anagram_index)