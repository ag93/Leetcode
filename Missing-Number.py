class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_nums = [i for i in range(len(nums)+1)]
        answer = set(all_nums) - set(nums)
        
        return(list(answer)[0])