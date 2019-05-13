class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        maxi = max(len(x), len(y))

        x = x.zfill(maxi)
        y = y.zfill(maxi)
        count = 0
        for i in range(0, maxi):
            if x[i] != y[i]:
                count = count + 1
            
        return(count)
    
    #return bin(x^y).count('1')