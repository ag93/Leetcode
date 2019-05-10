class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
            neg = True
            x = x * -1
        s = str(x)[::-1]
        n = int(s)
        if neg:
            n = n*-1
        if(abs(n) > (2 ** 31 - 1)):
            return 0
        return n