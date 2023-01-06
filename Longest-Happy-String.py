def longestDiverseString(a, b, c):
    """
    :type a: int
    :type b: int
    :type c: int
    :rtype: str
    """
    count = {
            'a': a,
            'b': b,
            'c': c
        }
        
    valid = [v for v in count if count[v]>0]    # All chars in count valid to begin with
    s = ''
    while valid:
        choice = max(valid, key=lambda x: count[x])    # Make a greedy choice by choosing the most available char
        s += choice
        count[choice] -= 1   # Reduce char count to indicate use of it
        valid = [v for v in count if count[v]>0]   # Recompute valid
        if len(s) > 1 and s[-1] == s[-2]:   # Check for restriction of last 2 chars being the same to remove it to avoid `aaa` or `bbb` or `ccc`
            valid.remove(choice)                                           
    return s

if __name__ == "__main__":
    a = 100
    b = 99
    c = 99

    print(longestDiverseString(a, b, c))