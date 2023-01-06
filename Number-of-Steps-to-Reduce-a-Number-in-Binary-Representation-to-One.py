def numOfSteps(s):
    # power = len(s)-1
    # decimal = 0
    # for number in s:
    #     decimal += int(number) * pow(2, power)
    #     power -= 1

    s = int(s, 2)
    count = 0
    while s!=1:
        if s%2 == 0:
            s = s/2
            count += 1
        else:
            s += 1
            count +=1
    return count

if __name__ == "__main__":
    print(numOfSteps("1"))