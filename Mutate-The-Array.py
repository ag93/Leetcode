def mutateTheArray(n, a):
    if len(a) == 0:
        return(a)

    if len(a) < 2:
        return(a)

    b = [0] * len(a)


    b[0] = a[0]+a[1]
    b[-1] = a[-1] + a[len(a) - 2]

    for i in range(1, len(a)-1):
        b[i] = a[i-1] + a[i] + a[i+1]

    return(b)