def alternatingSort(a):
    import math
    b = [0]*len(a)

    b[0] = a[0]
    
    if len(a) >= 2:
        b[1] = a[-1]
        for i in range(2, len(a)):
            if i%2 == 0:
                b[i] = a[int(i/2)]
            else:
                b[i] = a[-math.ceil(i/2)]

    return sorted(set(b)) == b