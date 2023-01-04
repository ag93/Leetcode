def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """

    sList = s.split(" ")
    result = ""
    for st in sList:
        result += st[::-1] + " "

    return result[:-1]

if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    print(reverseWords(s))