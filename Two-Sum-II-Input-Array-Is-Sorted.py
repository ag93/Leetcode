def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    hashmap = {}

    for i in range(len(numbers)):
        x = target - numbers[i]
        if x in hashmap:
            return([hashmap[x]+1, i+1])
        else:
            hashmap[numbers[i]] = i


if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9

    print(twoSum(numbers, target))