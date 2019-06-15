class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in xrange(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            two_sum_sols = self.two_sum(nums[i + 1:],-nums[i])
            for sol in two_sum_sols:
                res.append([nums[i]] + sol)
        return res
    
    
    def two_sum(self,nums,target):
        l,r = 0,len(nums) - 1
        res = []
        while l < r:
            if nums[l] + nums[r] == target:
                res.append([nums[l],nums[r]])
                l_val = nums[l]
                while l < r and nums[l] == l_val:
                    l += 1
                r_val = nums[r]
                while l < r and nums[r] == r_val:
                    r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
        return res