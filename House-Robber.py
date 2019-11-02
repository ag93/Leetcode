class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max = 0
        currMax = 0
        
        for i in range(len(nums)):
            temp = currMax
            currMax = max(prev_max + nums[i], currMax)
            prev_max = temp
            
        return currMax