def minCost(colors, neededTime):
    """
    :type colors: str
    :type neededTime: List[int]
    :rtype: int
    """

    if len(colors) == 1:
        return 0

    result = 0
    mapped = list(zip(colors, neededTime))
    start = 0
    end = 1

    while end<len(colors):
        if mapped[start][0] != mapped[end][0]:
            start += 1
            end += 1

        while end<len(colors) and mapped[start][0] == mapped[end][0]:
            end += 1
        
        #print(colors[start:end])
        if len(neededTime[start:end]) > 1:
            result += (sum(neededTime[start:end]) - max(neededTime[start:end]))
            start = end
            end = start+1
        #print(start,end)

    return (result)
if __name__ == "__main__":
    colors = "ababcbcaccbccbabbccaccbbbbbcbcaccbaacccbcbaabbcc"
    neededTime = [7,28,38,21,10,24,32,39,22,28,31,14,37,17,12,32,23,7,38,10,35,1,3,5,35,30,32,15,9,34,15,25,25,12,18,33,27,7,33,16,33,32,17,21,14,21,31,6]

    print(minCost(colors, neededTime))
