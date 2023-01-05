def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        map = {}

        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                return True
        
        return False

if __name__ == "__main__":
    nums = [1,1,1,3,3,4,3,2,4,2]

    print(containsDuplicate(nums))