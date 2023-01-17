def minFlipsMonoIncr(s):
    """
    :type s: str
    :rtype: int
    """
    ones = 0
    change = 0
    for i in s:
        if i == "0":
            if ones == 0:
                pass
            else:
                change += 1
        else:
            ones +=1
        change = min(change,ones)
    return change

if __name__ == "__main__":
    s = "00110"
    print(minFlipsMonoIncr(s))
