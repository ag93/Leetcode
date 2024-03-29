def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s)-1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    print(s)

if __name__ == "__main__":
    s = ["H","a","n","n","a","h"]
    reverseString(s)