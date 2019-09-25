def longestPalindrome(s):
    if (s == None or len(s) < 1):
        return ""
    start = 0
    end = 0
    for i in range(0, len(s)):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i + 1)
        len_ = max(len1, len2)
        if (len_ > end - start):
            start = i - (len_ - 1) // 2
            end = i + len_ // 2
    
    return s[start:end+1]

def expandAroundCenter(s, left, right):
    L = left
    R = right
    while (L >= 0 and R < len(s) and s[L] == s[R]):
        L-=1
        R+=1
    return(R - L - 1)
    
    
inputStream = 'xyzzyabc'
print(longestPalindrome(inputStream))