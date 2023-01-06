def sumZero(n):
    """
    :type n: int
    :rtype: List[int]
    """
    result = []
    for i in range(1, n//2+1):
        result.append(i)
        result.append(-i)

    if n%2 != 0:
        result.append(0)
    return(result)


if __name__ == '__main__':
    print(sumZero(69))