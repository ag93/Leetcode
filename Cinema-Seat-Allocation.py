def maxNumberOfFamilies(n, reservedSeats):
    """
    :type n: int
    :type reservedSeats: List[List[int]]
    :rtype: int
    """
    theater = {}
    for row, seat in reservedSeats:
        if row not in theater:
            theater[row] = [0]*10
            theater[row][seat-1] = 1
        else:
            theater[row][seat-1] = 1
    count = 0 
    theaterRows = theater.values()
    count += (n - len(theaterRows)) * 2

    for row in theaterRows:
        print(row)
        if row[1:9] == [0,0,0,0,0,0,0,0]:
            count += 2
        elif row[3:7] == [0,0,0,0] or row[1:5] == [0,0,0,0] or row[5:9] == [0,0,0,0]:
            count+=1
    return(count)
    
if __name__ == "__main__":
    n = 3
    reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
    print(maxNumberOfFamilies(n, reservedSeats))