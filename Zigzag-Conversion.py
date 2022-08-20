def convert(s, numRows):
    if numRows == 1:
        return s 

    finalStr = ''
    #Init Dict where each key represents a row
    dict = {}
    for i in range(1, numRows+1):
        dict[i] = ''

    #Elevator Logic!?
    decrement = False
    i = 1
    for letter in s:
        dict[i] += letter
        if(decrement):
            i = i - 1
        else:
            i = i + 1

        if i == numRows:
            decrement = True

        elif i == 1:
            decrement = False        

    for i in range(1, numRows+1):
        finalStr += dict[i]

    return(finalStr)



if __name__ == '__main__':
    print(convert('AB', 1))