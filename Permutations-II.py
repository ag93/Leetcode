class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations 
        perm = list(permutations(nums,len(nums)))
        return(list(set(perm)))
        