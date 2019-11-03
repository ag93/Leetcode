class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left_indexes = {}
        right_indexes = {}
        count = {}
        
        for i,x in enumerate(nums):
            if x not in left_indexes:
                left_indexes[x] = i
            right_indexes[x] = i
            count[x] = count.get(x, 0) + 1
            
        result = len(nums)
        degree = max(count.values())
        
        for x in count:
            if count[x] == degree:
                result = min(result, right_indexes[x] - left_indexes[x] + 1)
                
        return result