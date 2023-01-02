def confusingNumber(n):
        """
        :type n: int
        :rtype: bool
        """

        validDict = {"0":"0","1":"1","6":"9","8":"8","9":"6"}
        result = ""
        for number in str(n):
            if number not in validDict:
                return False

            else:
                result += validDict[number]
      
        return int(result[::-1]) != n  


if __name__ == "__main__":
    print(confusingNumber(11111))