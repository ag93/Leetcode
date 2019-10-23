def extractEachKth(inputArray, k):
    for item in (n for n in range(len(inputArray)) if (n+1)%k == 0):
        inputArray[item] = 'del'
    return([value for value in inputArray if value != 'del'])