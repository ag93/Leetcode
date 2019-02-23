class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations 
        perm = list(permutations(nums,len(nums)))
        return(perm)