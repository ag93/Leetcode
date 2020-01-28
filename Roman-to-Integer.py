class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        last = "M"
        res = 0
        
        for symbol in s:
            res += map[symbol]
            if map[symbol] > map[last]:
                res -= 2 * map[last]
            last = symbol
        
        return res