def moveZeroes(nums):
    count = 0
    for i in range(len(nums)):
        if (nums[i] != 0): 
            nums[count], nums[i] = nums[i], nums[count] #Swap the non zero element with count of 0 as index from L -> R
            count+=1


    # for num in nums:
    #     if num == 0:
    #         nums.remove(0)
    #         nums.append(0) 
    # 
    # ------------------------------------------------------------
        # result = []
        # zeros = 0

        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         result.append(nums[i])
        #     else:
        #         zeros += 1
        # nums[:] = result[:] + [0]*zeros   

    print(nums)

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    moveZeroes(nums)
