class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:    
            return 0
        if s[0] == '0':
            return 0
        first, second = 1, 1
        for i in range(2, len(s)+1):
            newsecond = 0
            if s[i-1] != '0':
                newsecond = second
            if '10' <= s[i-2:i] <= '26':
                newsecond += first
            first, second = second, newsecond
        return second