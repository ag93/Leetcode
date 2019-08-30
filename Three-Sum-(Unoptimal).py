class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_result =[]
        flag = True
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if(nums[i]+nums[j]+nums[k] == 0):
                        temp = [nums[i],nums[j],nums[k]]                    
                        if flag:
                            result.append(temp)
                            sorted_result.append(sorted(temp))
                            flag = False
                        else:
                            if(sorted(temp) not in sorted_result):
                                result.append(temp)
                                sorted_result.append(sorted(temp))
        return result