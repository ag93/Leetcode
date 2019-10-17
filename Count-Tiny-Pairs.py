def countTinyPairs(a, b, k):
    count = 0
    for i in range (len(a)):
        if i == 0:
            temp = str(a[i]) + str(b[-1])
        else:
            temp = str(a[i]) + str(b[-i-1])
        if int(temp) < k:
            count += 1

    return(count)