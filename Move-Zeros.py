class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        count = 0
        for i in range(len(nums)):
            if (nums[i] != 0): 
                nums[count], nums[i] = nums[i], nums[count] #Swap the non zero element with count of 0 as index from L -> R
                count+=1
