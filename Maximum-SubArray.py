def maxSubArray(nums):
    current_max = nums[0]
    global_max = nums[0]
        
    for i in range(1,len(nums)):
        current_max = max(nums[i],nums[i]+current_max)
        if current_max > global_max:
            global_max = current_max
            
    return global_max

    # max_subarray = -math.inf
    # for i in range(len(nums)):
    #     current_subarray = 0
    #     for j in range(i, len(nums)):
    #         current_subarray += nums[j]
    #         max_subarray = max(max_subarray, current_subarray)    
    # return max_subarray


if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))