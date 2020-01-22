class Solution:
    def myAtoi(self, str: str) -> int:       
        map = {
            "0" : 0,
            "1" : 1,
            "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9,
        }
        
        negative = False
        number = 0
        
        start = 0
        str = str.strip()
        
        if len(str) == 0:
            return 0
        
        if str[0] == "-":
            negative = True
            start = 1
        
        if str[0] == "+":
            negative = False
            start = 1   
        
        for i in range(start, len(str)):
            if str[i] in map.keys():
                number *= 10
                number += map[str[i]]
            else:
                return self.validate(number, negative)
        
        return(self.validate(number, negative))

    def validate(self, num, neg):
        if neg:
            if 0-num < -2147483648:
                return -2147483648
            else:
                return 0-num
        else:
            if num > 2147483647:
                return 2147483647
            else:
                return num