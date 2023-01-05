def findMinArrowShots(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    points.sort(key = lambda x : x[1])
    current_end = points[0][1]
    arrows = 1

    for start, end in points:
        if start > current_end:
            arrows += 1
            current_end = end

    return(arrows)

if __name__ == "__main__":
    points = [[10,16],[2,8],[1,6],[7,12]]
    print(findMinArrowShots(points))