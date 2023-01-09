def reverseWords(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """

    def reverserEachWord(s):
        n = len(s)
        start = end = 0
        
        while start < n:
            while end < n and s[end] != ' ':
                end += 1
            reverse(s, start, end - 1)
            start = end + 1
            end += 1

    def reverse(s, start, end):
        while start<end:
            s[start], s[end] = s[end], s[start]   
            start+=1
            end-=1

    reverse(s, 0, len(s)-1)
    reverserEachWord(s)
    print(s)
    

if __name__ == "__main__":
    s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    print(reverseWords(s))