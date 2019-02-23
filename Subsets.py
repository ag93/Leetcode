class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = [[]]
        
        for i in nums:
            answer = answer + [[i] + temp for temp in answer]
        return answer