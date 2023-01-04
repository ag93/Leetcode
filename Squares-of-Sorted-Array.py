# class Solution(object):
#     def sortedSquares(self, A):
#         return sorted(x*x for x in A)

def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    left = 0
    right = n-1

    result = [0]*n

    for i in range(n-1, -1, -1):
        leftSquare = nums[left]*nums[left]
        rightSquare = nums[right]*nums[right]
        if leftSquare > rightSquare:
            result[i] = leftSquare
            left+=1
        else:
            result[i] = rightSquare
            right-=1

    return result

if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    print(sortedSquares(nums))
