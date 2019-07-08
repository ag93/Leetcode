class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_5, change_10, change_20 = 0, 0, 0
        for i in bills:
            if i == 5:
                change_5 += 1
            elif i == 10 and change_5: 
                change_5 -= 1
                change_10 += 1
            elif i == 20 and change_5 and change_10:
                change_20 += 1
                change_10 -= 1
                change_5 -= 1
            elif i == 20 and change_5 > 2:
                change_20 += 1
                change_5 -= 3      
            else:
                return False
        return True