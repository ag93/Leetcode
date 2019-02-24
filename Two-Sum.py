class Solution:
    def twoSum(self, nums, target):
        dict = {}
        n = len(nums)
        for i in range(n):
            x = target - nums[i]
            if x in dict:
                return [dict[x], i]
            else:
                dict[nums[i]] = i